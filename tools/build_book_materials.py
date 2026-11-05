#!/usr/bin/env python3
"""Build the two brick practices using ORIGINAL Hour3 PNGs, never substitutes.

Does not complete Torus/Kyle activities or claim Unity validation.
Run only after obtaining the companion archive, e.g.
 python tools/build_book_materials.py --albedo '/path/Brick_Texture.png' --normal '/path/Brick_Normal.png'
"""
import argparse,hashlib,json,shutil
from pathlib import Path
import build_native_intro as native
ROOT=Path(__file__).resolve().parents[1]

def uid(key):return hashlib.md5(('uniytu/hour03/'+key).encode()).hexdigest()
def write_texture(source,target,normal=False):
    shutil.copyfile(source,target)
    guid=uid(target.name)
    meta=f'''fileFormatVersion: 2
guid: {guid}
TextureImporter:
  fileIDToRecycleName: {{}}
  externalObjects: {{}}
  serializedVersion: 5
  mipmaps:
    mipMapMode: 0
    enableMipMap: 1
    sRGBTexture: {0 if normal else 1}
    linearTexture: 0
    fadeOut: 0
    borderMipMap: 0
    mipMapsPreserveCoverage: 0
    alphaTestReferenceValue: 0.5
    mipMapFadeDistanceStart: 1
    mipMapFadeDistanceEnd: 3
  bumpmap:
    convertToNormalMap: 0
    externalNormalMap: 0
    heightScale: 0.25
    normalMapFilter: 0
  isReadable: 0
  grayScaleToAlpha: 0
  generateCubemap: 6
  cubemapConvolution: 0
  seamlessCubemap: 0
  textureFormat: 1
  maxTextureSize: 2048
  textureSettings:
    serializedVersion: 2
    filterMode: 1
    aniso: 3
    mipBias: -1
    wrapU: 0
    wrapV: 0
    wrapW: 0
  nPOTScale: 1
  lightmap: 0
  compressionQuality: 50
  spriteMode: 0
  textureType: {1 if normal else 0}
  textureShape: 1
  alphaUsage: 1
  alphaIsTransparency: 0
  userData:
  assetBundleName:
  assetBundleVariant:
'''
    Path(str(target)+'.meta').write_text(meta)
    return guid

def material(path,albedo,normal=None,smooth=0,tiling=(3,3)):
    guid=uid(path.stem)
    normalref=f'{{fileID: 2800000, guid: {normal}, type: 3}}' if normal else '{fileID: 0}'
    text=f'''%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!21 &2100000
Material:
  serializedVersion: 6
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_Name: {path.stem}
  m_Shader: {{fileID: 46, guid: 0000000000000000f000000000000000, type: 0}}
  m_ShaderKeywords: {'_NORMALMAP' if normal else ''}
  m_LightmapFlags: 4
  m_EnableInstancingVariants: 0
  m_DoubleSidedGI: 0
  m_CustomRenderQueue: -1
  stringTagMap: {{}}
  disabledShaderPasses: []
  m_SavedProperties:
    serializedVersion: 3
    m_TexEnvs:
    - _MainTex:
        m_Texture: {{fileID: 2800000, guid: {albedo}, type: 3}}
        m_Scale: {{x: {tiling[0]}, y: {tiling[1]}}}
        m_Offset: {{x: 0, y: 0}}
    - _BumpMap:
        m_Texture: {normalref}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    m_Floats:
    - _BumpScale: 1
    - _Cutoff: 0.5
    - _DstBlend: 0
    - _Glossiness: {smooth}
    - _GlossMapScale: {smooth}
    - _Metallic: 0
    - _Mode: 0
    - _SrcBlend: 1
    - _ZWrite: 1
    m_Colors:
    - _Color: {{r: 1, g: 1, b: 1, a: 1}}
    - _EmissionColor: {{r: 0, g: 0, b: 0, a: 1}}
'''
    path.write_text(text)
    Path(str(path)+'.meta').write_text(f'fileFormatVersion: 2\nguid: {guid}\nNativeFormatImporter:\n  externalObjects: {{}}\n  mainObjectFileID: 2100000\n  userData:\n  assetBundleName:\n  assetBundleVariant:\n')
    return guid

def bind_material(serialized,guid):
    return serialized.replace('fileID: 10303, guid: '+native.MATERIAL_GUID+', type: 0','fileID: 2100000, guid: '+guid+', type: 2')

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--albedo',type=Path,required=True);p.add_argument('--normal',type=Path,required=True);a=p.parse_args()
    for source,required in [(a.albedo,'Brick_Texture.png'),(a.normal,'Brick_Normal.png')]:
        if not source.is_file():p.error('Original companion file missing: '+str(source))
        if source.name!=required:p.error('Expected original filename '+required)
        if source.read_bytes()[:8]!=b'\x89PNG\r\n\x1a\n':p.error('Not a PNG: '+str(source))
    d=ROOT/'rebuild/Hour03';
    for folder in ['Assets/Scenes','Assets/Materials','Assets/Textures','ProjectSettings']:(d/folder).mkdir(parents=True,exist_ok=True)
    ag=write_texture(a.albedo,d/'Assets/Textures/Brick_Texture.png');ng=write_texture(a.normal,d/'Assets/Textures/Brick_Normal.png',True)
    wallmat=material(d/'Assets/Materials/BrickWall.mat',ag,tiling=(3,1))
    camera=native.camera((0,1,-13))
    wall=bind_material(native.primitive(300,'Cube',pos=(0,1,-5),scale=(5,2,1)),wallmat)
    scenes=[native.save_scene(d,'02_BrickWall',camera+native.light()+wall)]
    names=['DiffuseBrick','SpecularBrick','BumpedBrick','BumpedSpecularBrick'];points=[(1,2,-5),(-1,0,-5),(1,0,-5),(-1,2,-5)]
    body=camera+native.light(pos=(0,10,-10)).replace(native.vec(native.quat((50,-30,0)),'xyzw'),native.vec(native.quat((30,-180,0)),'xyzw')).replace(native.vec((50,-30,0)),native.vec((30,-180,0)))
    for i,(name,pos) in enumerate(zip(names,points)):
        mg=material(d/'Assets/Materials'/f'{name}.mat',ag,ng if i>=2 else None,.6 if i%2 else 0)
        body+=bind_material(native.primitive(300+i*100,name,kind='Sphere',pos=pos,scale=(2,2,2),order=i+2),mg)
    scenes.append(native.save_scene(d,'03_ExerciseMaterials',body))
    (d/'ProjectSettings/ProjectVersion.txt').write_text('m_EditorVersion: 2018.1.0f1\n')
    (d/'ProjectSettings/EditorBuildSettings.asset').write_text('%YAML 1.1\n%TAG !u! tag:unity3d.com,2011:\n--- !u!1045 &1\nEditorBuildSettings:\n  m_ObjectHideFlags: 0\n  serializedVersion: 2\n  m_Scenes:\n'+''.join('  - enabled: 1\n    path: '+scene['path']+'\n    guid: '+scene['guid']+'\n' for scene in scenes)+'  m_configObjects: {}\n')
    (d/'ОТКРЫТЬ.md').write_text('''# Час 3 — кирпичные материалы (часть главы)

Две сохранённые сцены: стена с Albedo tiling3×1 и четыре сферы Standard/Opaque tiling3×3, Smoothness0/.6, Metallic0; две сферы с настоящей normal map TextureImporter NormalMap.

Файлы текстур скопированы из указанных исходных PNG без перерисовки. UV у встроенных Cube/Sphere уже существуют. Это не полная глава: практикумы Torus.fbx с Import Scale100 и Robot Kyle ещё требуют соответствующих исходников.

Открыть сцену можно до Play. В Unity 2018.1.0f1 ещё не проверено: нужно проверить импорт, Inspector материалов и normal map, видимые различия рельефа/бликов, сохранение и повторное открытие сцены.
''')
    (d/'original-assets.json').write_text(json.dumps({source.name:{'sha256':hashlib.sha256(source.read_bytes()).hexdigest()} for source in [a.albedo,a.normal]},indent=2)+'\n')
    print('Wrote two native Hour03 scenes using supplied originals; Torus/Kyle and Unity runtime checks remain incomplete.')
if __name__=='__main__':main()
