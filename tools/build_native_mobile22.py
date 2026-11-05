#!/usr/bin/env python3
"""Native saved mobile practica. Actual USB/Remote/device checks are mandatory, UNRUN."""
from pathlib import Path
import json
import build_native_intro as n
from build_native_scripting import write_script,behaviour,attach_camera
ROOT=Path(__file__).resolve().parents[1]

def mb(i,go,script,fields):return behaviour(i,go,script,fields)
def rect(i,go,parent=0,children=(),size=(160,40)):
    return f'''--- !u!224 &{i}
RectTransform:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {{fileID: 0}}
  m_PrefabInternal: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_Children:'''+ ('\n'+''.join(f'  - {{fileID: {c}}}\n' for c in children) if children else ' []\n')+f'''  m_Father: {{fileID: {parent}}}
  m_RootOrder: 0
  m_AnchorMin: {{x: 0.5, y: 0.5}}
  m_AnchorMax: {{x: 0.5, y: 0.5}}
  m_AnchoredPosition: {{x: 0, y: 0}}
  m_SizeDelta: {{x: {size[0]}, y: {size[1]}}}
  m_Pivot: {{x: 0.5, y: 0.5}}
'''

def button_scene():
    result=n.camera()+n.light()
    result+=n.gameobject(1000,'Canvas',[1001,1002,1003])+rect(1001,1000,children=(1101,))
    result+='''--- !u!223 &1002
Canvas:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_GameObject: {fileID: 1000}
  m_Enabled: 1
  serializedVersion: 3
  m_RenderMode: 0
  m_Camera: {fileID: 0}
  m_PlaneDistance: 100
  m_PixelPerfect: 0
  m_ReceivesEvents: 1
  m_OverrideSorting: 0
  m_OverridePixelPerfect: 0
  m_SortingBucketNormalizedSize: 0
  m_AdditionalShaderChannelsFlag: 0
  m_SortingLayerID: 0
  m_SortingOrder: 0
  m_TargetDisplay: 0
'''
    result+=mb(1003,1000,'dc42784cf147c0c48a680349fa168899','''  m_IgnoreReversedGraphics: 1
  m_BlockingObjects: 0
  m_BlockingMask:
    serializedVersion: 2
    m_Bits: 4294967295
''')
    result+=n.gameobject(1100,'Button',[1101,1102,1103,1104])+rect(1101,1100,1001,(1201,))
    result+='''--- !u!222 &1102
CanvasRenderer:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_GameObject: {fileID: 1100}
  m_CullTransparentMesh: 0
'''
    result+=mb(1103,1100,'fe87c0e1cc204ed48ad3b37840f39efcb','''  m_Material: {fileID: 0}
  m_Color: {r: 1, g: 1, b: 1, a: 1}
  m_RaycastTarget: 1
  m_OnCullStateChanged:
    m_PersistentCalls:
      m_Calls: []
  m_Sprite: {fileID: 0}
  m_Type: 0
  m_PreserveAspect: 0
  m_FillCenter: 1
  m_FillMethod: 4
  m_FillAmount: 1
  m_FillClockwise: 1
  m_FillOrigin: 0
''')
    result+=mb(1104,1100,'4e29b1a8efbd4b44bb3f3716e73f07ff','''  m_Navigation:
    m_Mode: 3
    m_SelectOnUp: {fileID: 0}
    m_SelectOnDown: {fileID: 0}
    m_SelectOnLeft: {fileID: 0}
    m_SelectOnRight: {fileID: 0}
  m_Transition: 1
  m_Colors:
    m_NormalColor: {r: 1, g: 1, b: 1, a: 1}
    m_HighlightedColor: {r: 0.88, g: 0.88, b: 0.88, a: 1}
    m_PressedColor: {r: 1, g: 0, b: 0, a: 1}
    m_DisabledColor: {r: 0.78, g: 0.78, b: 0.78, a: 0.5}
    m_ColorMultiplier: 1
    m_FadeDuration: 0.1
  m_SpriteState:
    m_HighlightedSprite: {fileID: 0}
    m_PressedSprite: {fileID: 0}
    m_DisabledSprite: {fileID: 0}
  m_AnimationTriggers:
    m_NormalTrigger: Normal
    m_HighlightedTrigger: Highlighted
    m_PressedTrigger: Pressed
    m_DisabledTrigger: Disabled
  m_Interactable: 1
  m_TargetGraphic: {fileID: 1103}
  m_OnClick:
    m_PersistentCalls:
      m_Calls: []
''')
    result+=n.gameobject(1200,'Text',[1201,1202,1203])+rect(1201,1200,1101,size=(160,40))
    result+='''--- !u!222 &1202
CanvasRenderer:
  m_ObjectHideFlags: 0
  m_PrefabParentObject: {fileID: 0}
  m_PrefabInternal: {fileID: 0}
  m_GameObject: {fileID: 1200}
  m_CullTransparentMesh: 0
'''
    result+=mb(1203,1200,'5f7201a12d95ffc409449d95f23cf332','''  m_Material: {fileID: 0}
  m_Color: {r: 0.2, g: 0.2, b: 0.2, a: 1}
  m_RaycastTarget: 0
  m_FontData:
    m_Font: {fileID: 12800000, guid: 0000000000000000e000000000000000, type: 0}
    m_FontSize: 14
    m_FontStyle: 0
    m_BestFit: 0
    m_MinSize: 10
    m_MaxSize: 40
    m_Alignment: 4
    m_AlignByGeometry: 0
    m_RichText: 1
    m_HorizontalOverflow: 0
    m_VerticalOverflow: 0
    m_LineSpacing: 1
  m_Text: Button
''')
    result+=n.gameobject(1300,'EventSystem',[1301,1302,1303])+n.transform(1301,1300,order=3)
    result+=mb(1302,1300,'76c392e42b5098c458856cdf6ecaaaaa1','''  m_FirstSelected: {fileID: 0}
  m_sendNavigationEvents: 1
  m_DragThreshold: 10
''')
    result+=mb(1303,1300,'4f231c4fb786f3946a6b90b886c48677','''  m_HorizontalAxis: Horizontal
  m_VerticalAxis: Vertical
  m_SubmitButton: Submit
  m_CancelButton: Cancel
  m_InputActionsPerSecond: 10
  m_RepeatDelay: 0.5
  m_ForceModuleActive: 0
''')
    return result

def attach_object(serialized,go,comp,guid):
    # Insert the attached script into the GameObject component list.
    marker=f'  - component: {{fileID: {go+4}}}\n'
    return serialized.replace(marker,marker+f'  - component: {{fileID: {comp}}}\n',1)+behaviour(comp,go,guid)

def main():
    p=n.OUT/'Hour22';(p/'Assets/Scripts').mkdir(parents=True,exist_ok=True)
    accel=write_script(p,'AccelerometerScript','''using UnityEngine;
public class AccelerometerScript : MonoBehaviour
{
    void Update()
    {
        float xMove = Input.acceleration.x * Time.deltaTime;
        float zMove = -Input.acceleration.z * Time.deltaTime;
        transform.Translate(xMove, 0f, zMove);
    }
}''')
    touches=write_script(p,'TouchScript','''using UnityEngine;
public class TouchScript : MonoBehaviour
{
    void OnGUI()
    {
        if (Input.touchCount == 0) GUI.Label(new Rect(5, 5, 500, 30), "No touch data. Connect a real Unity Remote device.");
        for (int i = 0; i < Input.touchCount; i++)
        {
            Touch touch = Input.GetTouch(i);
            float x = 5 + i * 130;
            GUI.Label(new Rect(x, 5, 130, 25), "ID: " + touch.fingerId);
            GUI.Label(new Rect(x, 30, 130, 25), "Phase: " + touch.phase);
            GUI.Label(new Rect(x, 55, 130, 25), "Taps: " + touch.tapCount);
            GUI.Label(new Rect(x, 80, 130, 25), "X: " + touch.position.x);
            GUI.Label(new Rect(x, 105, 130, 25), "Y: " + touch.position.y);
        }
    }
}''')
    exact=write_script(p,'InputScript','''using UnityEngine;
// Printed exercise: the book assumes touch IDs 0,1,2. See optional stable variant.
public class InputScript : MonoBehaviour
{
    void Update()
    {
        foreach (Touch touch in Input.touches)
        {
            float xMove = touch.deltaPosition.x * 0.05f;
            float yMove = touch.deltaPosition.y * 0.05f;
            if (touch.fingerId == 0 && gameObject.name == "Cube1") transform.Translate(xMove,yMove,0f);
            if (touch.fingerId == 1 && gameObject.name == "Cube2") transform.Translate(xMove,yMove,0f);
            if (touch.fingerId == 2 && gameObject.name == "Cube3") transform.Translate(xMove,yMove,0f);
        }
    }
}''')
    # Keep a robust equivalent in a clearly separate comparison scene.
    stable=write_script(p,'StableInputScript','''using UnityEngine;
using System.Collections.Generic;

// Separate comparison variant: fingers retain their Cube until released.
// This is deliberately not a silent change to the printed InputScript example.
public class StableInputScript : MonoBehaviour
{
    void Update()
    {
        TouchRouting.UpdateRouting();
        foreach (Touch touch in Input.touches)
        {
            int index = TouchRouting.CubeFor(touch.fingerId);
            if (name == "Cube" + (index + 1) && touch.phase == TouchPhase.Moved)
                transform.Translate(touch.deltaPosition.x * .05f,
                    touch.deltaPosition.y * .05f, 0f);
        }
    }
}

public static class TouchRouting
{
    static readonly Dictionary<int, int> fingers = new Dictionary<int, int>();
    static int frame = -1;

    public static void UpdateRouting()
    {
        // Three Cube components share one update of the mapping per frame.
        if (frame == Time.frameCount) return;
        frame = Time.frameCount;
        if (Input.touchCount == 0) { fingers.Clear(); return; }

        var remove = new List<int>();
        foreach (var pair in fingers)
        {
            bool found = false;
            foreach (Touch touch in Input.touches)
                if (touch.fingerId == pair.Key && touch.phase != TouchPhase.Ended
                        && touch.phase != TouchPhase.Canceled)
                    found = true;
            if (!found) remove.Add(pair.Key);
        }
        foreach (int id in remove) fingers.Remove(id);

        foreach (Touch touch in Input.touches)
        {
            if (touch.phase == TouchPhase.Ended || touch.phase == TouchPhase.Canceled
                    || fingers.ContainsKey(touch.fingerId)) continue;
            for (int cube = 0; cube < 3; cube++)
            {
                if (fingers.ContainsValue(cube)) continue;
                fingers.Add(touch.fingerId, cube);
                break;
            }
        }
    }

    public static int CubeFor(int id)
    {
        int result;
        return fingers.TryGetValue(id, out result) ? result : -1;
    }
}''')
    def cubes(script):
        result=n.camera()+n.light()
        for i in range(3):
            go=1000+i*100
            result+=attach_object(n.primitive(go,'Cube'+str(i+1),pos=(-3+i*3,1,-5),order=i+2),go,go+5,script)
        return result
    scenes=[('01_UnityRemoteButton',button_scene()),
            ('02_Accelerometer',n.camera()+n.light()+attach_object(n.primitive(1000,'Cube'),1000,1005,accel)),
            ('03_TouchInformation',attach_camera([touches])),
            ('04_Exercise_BookInput',cubes(exact)),
            ('05_Exercise_StableFingerIds',cubes(stable))]
    n.build_project(22,scenes,'''# Час 22 — мобильный ввод

Версия: Unity 2018.1.0f1. Откройте отдельную сцену Assets/Scenes двойным щелчком. Геометрия и UI уже сохранены; их не создаёт генератор при Play.

| Книга | Сцена |
|---|---|
| Unity Remote, стр.422–423 | 01_UnityRemoteButton: настоящий Canvas/Button/EventSystem, Pressed Color красный. |
| Акселерометр, стр.425 | 02_Accelerometer: Cube в начале координат; AccelerometerScript, Translate(acceleration.x*deltaTime,0,-acceleration.z*deltaTime). |
| Касания, стр.427 | 03_TouchInformation: камера с TouchScript, ID/phase/tapCount/X/Y каждого касания. Колонки идут по индексу видимого касания, чтобы большие fingerId не уводили текст за экран. |
| Итоговое упражнение, стр.429–430 | 04_Exercise_BookInput: Cube1(-3,1,-5),Cube2(0,1,-5),Cube3(3,1,-5), исходная логика fingerId0/1/2 и deltaPosition*.05. |
| Отдельное сравнение устойчивого ввода | 05_Exercise_StableFingerIds: тот же результат для произвольных fingerId, привязка сохраняется до отпускания. Это явно обозначенное исправление ограничения книжного примера. |

Нужен физический телефон/USB с Unity Remote и подходящий Device в Edit → Project Settings → Editor → Unity Remote. Android/iOS SDK и платформа нужны, если дополнительно собираете приложение на устройство. В этой поставке настройки конкретного устройства не подменены фиктивными значениями. Десктопный клик проверяет только Button; он не проверяет акселерометр или мультитач. Мышиного заменителя касаний нет.

Нужно проверить на устройстве: нажатие меняет кнопку на красную; наклон перемещает Cube; видны ID/phase/координаты; три куба двигаются независимо; отпускание среднего пальца не переназначает оставшиеся; повторное касание занимает свободный куб в устойчивом варианте.

Структурные проверки не подтверждают импорт UI/компиляцию/Play/USB/Unity Remote. Все эти реальные проверки здесь UNRUN. Внешние графические текстуры глава не требует.
''')
    # UI navigation axes must exist even though other scenes use only touch input.
    axes=[]
    for name,negative,positive,altneg,altpos in [('Horizontal','left','right','a','d'),('Vertical','down','up','s','w'),('Submit','','return','','space'),('Cancel','','escape','','')]:
        axes.append(f'''  - serializedVersion: 3
    m_Name: {name}
    descriptiveName:
    descriptiveNegativeName:
    negativeButton: {negative}
    positiveButton: {positive}
    altNegativeButton: {altneg}
    altPositiveButton: {altpos}
    gravity: 3
    dead: 0.001
    sensitivity: 3
    snap: 0
    invert: 0
    type: 0
    axis: 0
    joyNum: 0
''')
    (p/'ProjectSettings/InputManager.asset').write_text(n.HEADER+'--- !u!13 &1\nInputManager:\n  m_ObjectHideFlags: 0\n  serializedVersion: 2\n  m_Axes:\n'+''.join(axes))
    manifest=json.loads((p/'scene_manifest.json').read_text());manifest.update(runtime_scripts=4,source_requirements=['22.1','22.2','22.3','22.E'],unity_import='UNRUN',phone_remote='UNRUN');(p/'scene_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print('Wrote native Hour22 scenes. Phone/Unity checks UNRUN.')
if __name__=='__main__':main()
