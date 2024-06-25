TOKEN = '6923133944:AAGOML81KKUckHHLXdbou52b4C6EBtX-Gms'

problems = {
    '🛜Интернет': {
        'callback_data': 'internet_problems',
        'subproblems': {
            'Отсутствует доступ в интернет': 'no_internet_access',
            'Отсутствие доступа к удаленным ресурсам': 'no_remote_access',
            'Проблема с доступом по каналам связи': 'communication_issue',
            'Настройка интернета': 'internet_setup',
            'Подключение и настройка сетевой папки': 'network_folder_setup',
            'Открытие особого доступа в интернет': 'special_internet_access'
        }
    },
    '🖥Компьютеры, серверы, периферия': {
        'callback_data': 'computer_problems',
        'subproblems': {
            'Не работает компьютерная техника': 'computer_not_working',
            'Не работает оргтехника': 'office_equipment_not_working',
            'Установка и настройка компьютерной техники': 'computer_setup',
            'Установка и настройка оргтехники': 'office_equipment_setup',
            'Обслуживание компьютерной техники': 'computer_maintenance',
            'Обслуживание оргтехники': 'office_maintenance',
            'Перенос пользовательских данных': 'data_transfer',
            'Составление дефектной ведомости': 'defect_documentation',
            'Техническое сопровождение': 'technical_support',
            'Выдача компьютерной техники и оргтехники': 'equipment_distribution',
            'Настройка удаленного доступа': 'remote_access_setup',
            'Закупка компьютерной техники и оргтехники': 'equipment_purchase',
            'Предоставление виртуальных серверов': 'virtual_servers_provision',
            'Выделение вычислительных ресурсов на кластере': 'compute_resources_allocation',
            'Заправка картриджей': 'cartridge_refilling',
            'Ремонт оргтехники': 'office_equipment_repair'
        }
    },
    '📶Корпоративная сеть': {
        'callback_data': 'network_problems',
        'subproblems': {
            'Не функционирует': 'network_not_functioning',
            'Настройка сетевого оборудования': 'network_equipment_setup',
            'Прокладка сети': 'network_cabling',
            'Изготовление патч-кордов': 'patch_cord_making',
            'Закупка сетевого оборудования и расходных материалов': 'network_equipment_purchase',
            'Выдача расходных материалов и сетевого оборудования': 'network_materials_distribution',
            'Запросить доступ к VPN-подключению к сети КФУ': 'vpn_access_request'
        }
    },
    '🎦Мониторинг работы web-камер': {
        'callback_data': 'webcam_problems',
        'subproblems': {
            'Плохое качество изображения': 'poor_image_quality',
            'Отсутствует изображение': 'no_image',
            'Подключение к камерам в аудиториях': 'auditorium_cameras_connection'
        }
    },
    '🖨Мультимедийное оборудование': {
        'callback_data': 'multimedia_problems',
        'subproblems': {
            'Не работает': 'multimedia_not_working',
            'Подключение и настройка установленного оборудования': 'multimedia_setup',
            'Предоставление и настройка оборудования без технического сопровождения мероприятия': 'multimedia_provision_no_support',
            'Предоставление и настройка оборудования с техническим сопровождением мероприятия': 'multimedia_provision_with_support',
            'Проведение видеоконференции': 'video_conferencing',
            'Закупка мультимедийного оборудования': 'multimedia_equipment_purchase',
            'Инструктаж пользователей работе с мультимедийным оборудованием': 'multimedia_user_instruction',
            'Составление дефектной ведомости для мультимедийного оборудования': 'multimedia_defects_documentation'
        }
    },
    '👨‍💻Прикладное программное обеспечение (ПО)': {
        'callback_data': 'application_software_problems',
        'subproblems': {
            'Ошибка при работе с ПО': 'software_error',
            'Установка и настройка ПО': 'software_installation',
            'Дополнительная настройка ПО': 'software_additional_setup',
            'Установка и настройка серверного ПО': 'server_software_setup',
            'Подключение и настройка Консультант Плюс': 'consultant_plus_setup',
            'Закупка ПО': 'software_purchase'
        }
    },
    '👨‍Системное программное обеспечение': {
        'callback_data': 'system_software_problems',
        'subproblems': {
            'Ошибки при загрузке ОС': 'os_loading_errors',
            'Ошибки при работе ОС': 'os_operational_errors',
            'Установка ОС': 'os_installation',
            'Дополнительная настройка ОС': 'os_additional_setup'
        }
    },
    '📞Телефония': {
        'callback_data': 'telephony_problems',
        'subproblems': {
            'Не работает устройство связи': 'communication_device_failure',
            'Отсутствует доступ': 'access_unavailable',
            'Установка и настройка устройств связи': 'communication_device_setup',
            'Выделение нового номера': 'new_number_allocation',
            'Перенос номера': 'number_transfer',
            'Открытие доступа к внутризоновой связи': 'local_call_access',
            'Открытие доступа к междугородней связи': 'intercity_call_access',
            'Открытие доступа к международной связи': 'international_call_access',
            'Открытие доступа к корпоративной мобильной связи': 'corporate_mobile_access',
            'Закупка телефонного оборудования': 'telephony_equipment_purchase'
        }
    }
}
