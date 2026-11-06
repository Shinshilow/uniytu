# Материалы для обслуживания

Основные пользовательские проекты — Hour01.zip…Hour24.zip в корне. Эти файлы не нужны для обычного открытия в Unity.

maintenance_sources.zip сохраняет генераторы/сборщик, проверенные простые сцены и дополнительные реализации. Распаковка в корень рабочего репозитория восстанавливает tools, rebuild и course_additions. Для повторной сборки нужен исходный Unity.zip, распакованный в /workspace/book-originals/extracted; UnityPy1.25.4 используется для чтения/записи TerrainData, PyYAML и tree-sitter — для файловых проверок. В этих инструментах пути соответствуют облачной рабочей среде, а не пользовательской установке Unity.

Сборочный порядок: python tools/assemble_book_course.py; python tools/complete_book_course.py; python tools/finalize_book_course.py; затем проверки и package_book_course.py. Программные контролы/инструкции в рабочих копиях дополнительно уточнены перед упаковкой; архивы HourNN являются точными опубликованными артефактами, SHA256 сохранены в manifest.json.

checks содержит сверку книги и результаты фактических файловых проверок. Ни один отчёт не подтверждает запуск Unity или готовность EXE. Оригинальный источник: https://github.com/Shinshilow/uniytu/releases/tag/book-files . SHA256 исходного Unity.zip: e81725573d2570ba1ba36d7d2f6acd9ac4176c8799c766ba5696c6bb15291192.
