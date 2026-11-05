# Повторная проверка нативных часов 01,02,07,08

Проверены фактические сохранённые сцены, ProjectSettings, MonoImporter metadata и исходники, а не только синтаксис генератора.

- 18 сцен прошли YAML-разбор, проверку локальных fileID, владельцев компонентов, parent/children, GUID скриптов и соответствия EditorBuildSettings.
- 40 дополнительных сверок относятся к заданиям книги: точные Transform Cube/Sphere, связь родителей, размещение требуемых скриптов на Main Camera либо Cube, явная ссылка CubeControlScript → Camera, все четыре оси ввода с правильными клавишами и индексами мыши.
- В часах01/02 нет MonoBehaviour и внешних материалов; геометрия существует до Play. Для этих глав книга не требует текстур.
- В часе07 три итоговых скрипта сохранены как отдельные компоненты Main Camera. HelloWorld и ImportantFunctions находятся в отдельных сценах. OperatorsStudy обозначен самостоятельным учебным примером; отсутствие оригинального EqualityAndOperations.cs не скрыто.
- В часе08 все формы FireBall возвращают95/75/20 по формуле исходников; локальный и целевой CubeScript следуют книжным Translate/Rotate на кадр. Итоговый CubeControlScript ссылается на существующую Camera; его клавиши не зависят от старого Lesson/CourseSetup.
- Просмотренные вызовы C# относятся к базовым API Unity2018: MonoBehaviour.print; Input.GetAxis/GetKey/GetKeyDown; Transform.Translate/Rotate/localScale; GameObject.Find. Избыточных Tilemap/Timeline/UI package-зависимостей нет.

Конкретных новых расхождений между аудитом и этими четырьмя проектами не выявлено; исходники не менялись. Проверка не подтверждает десериализацию Unity, компиляцию с его DLL, фактический Game view или поведение при реальном вводе. Эти действия **не запускались**.

JSON с отдельными сверками: native-hour01-02-07-08-semantic-review.json. Общий структурный результат: native-intro-scripting-review-structure.json.
