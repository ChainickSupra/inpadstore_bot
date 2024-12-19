from token1 import token
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

TOKEN = token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data='menu_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите категорию", reply_markup=reply_markup)

async def back_to_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Помощь", callback_data='menu_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите категорию", reply_markup=reply_markup)

async def menu_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Хочу задать вопрос касаемо работы плагина", callback_data='plugin_help')],
        [InlineKeyboardButton("Хочу сообщить об ошибке", callback_data='error_report')],
        [InlineKeyboardButton("Нужна помощь при установке/активации", callback_data='activation_help')],
        [InlineKeyboardButton("Назад", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите пункт, по которому вам нужна помощь:", reply_markup=reply_markup)

async def plugin_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Концепция", callback_data='menu_concept_plugin')],
        [InlineKeyboardButton("Архитектура", callback_data='menu_architect_plugin')],
        [InlineKeyboardButton("Конструктив", callback_data='menu_constructive_plugin')],
        [InlineKeyboardButton("ОВ и ВК", callback_data='menu_ov_vk_plugin')],
        [InlineKeyboardButton("Общие", callback_data='menu_general_plugin')],
        [InlineKeyboardButton("Боксы и отверстия", callback_data='menu_boxes_plugin')],
        [InlineKeyboardButton("Renga", callback_data='menu_renga_plugin')],
        [InlineKeyboardButton("Назад", callback_data='menu_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите из какой категории плагин, с которым вам нужна помощь:", reply_markup=reply_markup)

async def error_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Концепция", callback_data='menu_concept_error')],
        [InlineKeyboardButton("Архитектура", callback_data='menu_architect_error')],
        [InlineKeyboardButton("Конструктив", callback_data='menu_constructive_error')],
        [InlineKeyboardButton("ОВ и ВК", callback_data='menu_ov_vk_error')],
        [InlineKeyboardButton("Общие", callback_data='menu_general_error')],
        [InlineKeyboardButton("Боксы и отверстия", callback_data='menu_boxes_error')],
        [InlineKeyboardButton("Renga", callback_data='menu_renga_error')],
        [InlineKeyboardButton("Назад", callback_data='menu_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите из какой категории плагин, с которым вам нужна помощь:", reply_markup=reply_markup)

async def activation_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Ошибка при установке сборки", callback_data='installation_error')],
        [InlineKeyboardButton("Не получается зарегистрироваться", callback_data='registration_error')],
        [InlineKeyboardButton("Не получается ввести ключ активации", callback_data='activation_key_error')],
        [InlineKeyboardButton("Назад", callback_data='menu_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите категорию, по которой вам нужна помощь:", reply_markup=reply_markup)

async def menu_concept_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Инсоляция", callback_data='concept_insolation')],
        [InlineKeyboardButton("КЕО", callback_data='concept_keo')],
        [InlineKeyboardButton("Генерация парков", callback_data='concept_parks')],
        [InlineKeyboardButton("Генерация деревьев", callback_data='concept_trees')],
        [InlineKeyboardButton("Разлиновка модели", callback_data='concept_model')],
        [InlineKeyboardButton("3D сетки", callback_data='concept_3d')],
        [InlineKeyboardButton("БыстроТЭПы", callback_data='concept_tep')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='concept_areas')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_concept_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Инсоляция", callback_data='concept_insolation')],
        [InlineKeyboardButton("КЕО", callback_data='concept_keo')],
        [InlineKeyboardButton("Генерация парков", callback_data='concept_parks')],
        [InlineKeyboardButton("Генерация деревьев", callback_data='concept_trees')],
        [InlineKeyboardButton("Разлиновка модели", callback_data='concept_model')],
        [InlineKeyboardButton("3D сетки", callback_data='concept_3d')],
        [InlineKeyboardButton("БыстроТЭПы", callback_data='concept_tep')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='concept_areas')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_architect_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Определить помещение", callback_data='architect_room')],
        [InlineKeyboardButton("Расчет плинтуса", callback_data='architect_baseboard')],
        [InlineKeyboardButton("Отделка", callback_data='architect_finishing')],
        [InlineKeyboardButton("Копировать отделку", callback_data='architect_copy')],
        [InlineKeyboardButton("Проемы по дверям/окнам из связи", callback_data='architect_openings')],
        [InlineKeyboardButton("Соединение полов", callback_data='architect_floors')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='architect_areas')],
        [InlineKeyboardButton("Планировка", callback_data='architect_planning')],
        [InlineKeyboardButton("Округление площади", callback_data='architect_round')],
        [InlineKeyboardButton("Нумерация квартир", callback_data='architect_apartment')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_architect_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Определить помещение", callback_data='architect_room')],
        [InlineKeyboardButton("Расчет плинтуса", callback_data='architect_baseboard')],
        [InlineKeyboardButton("Отделка", callback_data='architect_finishing')],
        [InlineKeyboardButton("Копировать отделку", callback_data='architect_copy')],
        [InlineKeyboardButton("Проемы по дверям/окнам из связи", callback_data='architect_openings')],
        [InlineKeyboardButton("Соединение полов", callback_data='architect_floors')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='architect_areas')],
        [InlineKeyboardButton("Планировка", callback_data='architect_planning')],
        [InlineKeyboardButton("Округление площади", callback_data='architect_round')],
        [InlineKeyboardButton("Нумерация квартир", callback_data='architect_apartment')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_constructive_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Сборка арматуры", callback_data='constructive_assembly')],
        [InlineKeyboardButton("Создать разрезы и сечения", callback_data='constructive_sections')],
        [InlineKeyboardButton("Создание планов", callback_data='constructive_plans')],
        [InlineKeyboardButton("Создание контура", callback_data='constructive_contour')],
        [InlineKeyboardButton("Редактирование контура", callback_data='constructive_contour_redactor')],
        [InlineKeyboardButton("Расчет продавливания", callback_data='constructive_squeezing')],
        [InlineKeyboardButton("Создание каркасов", callback_data='constructive_frames')],
        [InlineKeyboardButton("Создание видов каркасов", callback_data='constructive_frametypes')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_constructive_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Сборка арматуры", callback_data='constructive_assembly')],
        [InlineKeyboardButton("Создать разрезы и сечения", callback_data='constructive_sections')],
        [InlineKeyboardButton("Создание планов", callback_data='constructive_plans')],
        [InlineKeyboardButton("Создание контура", callback_data='constructive_contour')],
        [InlineKeyboardButton("Редактирование контура", callback_data='constructive_contour_redactor')],
        [InlineKeyboardButton("Расчет продавливания", callback_data='constructive_squeezing')],
        [InlineKeyboardButton("Создание каркасов", callback_data='constructive_frames')],
        [InlineKeyboardButton("Создание видов каркасов", callback_data='constructive_frametypes')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_ov_vk_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Муфты/гильзы", callback_data='ov_vk_couplings')],
        [InlineKeyboardButton("Аэродинамика", callback_data='ov_vk_aero')],
        [InlineKeyboardButton("Создать виды систем", callback_data='ov_vk_systemtypes')],
        [InlineKeyboardButton("Спецификации систем", callback_data='ov_vk_systems')],
        [InlineKeyboardButton("Высотные отметки", callback_data='ov_vk_elevations')],
        [InlineKeyboardButton("Толщина стенки", callback_data='ov_vk_wall_thickness')],
        [InlineKeyboardButton("Диаметр изоляции", callback_data='ov_vk_isolation')],
        [InlineKeyboardButton("S изоляции", callback_data='ov_vk_S_isolation')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_ov_vk_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Муфты/гильзы", callback_data='ov_vk_couplings')],
        [InlineKeyboardButton("Аэродинамика", callback_data='ov_vk_aero')],
        [InlineKeyboardButton("Создать виды систем", callback_data='ov_vk_systemtypes')],
        [InlineKeyboardButton("Спецификации систем", callback_data='ov_vk_systems')],
        [InlineKeyboardButton("Высотные отметки", callback_data='ov_vk_elevations')],
        [InlineKeyboardButton("Толщина стенки", callback_data='ov_vk_wall_thickness')],
        [InlineKeyboardButton("Диаметр изоляции", callback_data='ov_vk_isolation')],
        [InlineKeyboardButton("S изоляции", callback_data='ov_vk_S_isolation')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_general_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Этажи и секции", callback_data='general_floors')],
        [InlineKeyboardButton("Подсчет узлов", callback_data='general_nodes')],
        [InlineKeyboardButton("Печать листов", callback_data='general_print')],
        [InlineKeyboardButton("Множественная печать", callback_data='general_multiplie_print')],
        [InlineKeyboardButton("Копировать спецификацию", callback_data='general_copy_spec')],
        [InlineKeyboardButton("Копировать параметры", callback_data='general_copy_params')],
        [InlineKeyboardButton("Параметры семейств", callback_data='general_params')],
        [InlineKeyboardButton("Копировать параметры арматуры", callback_data='general_copy_params_armature')],
        [InlineKeyboardButton("Комбинатор дверей", callback_data='general_doors')],
        [InlineKeyboardButton("Огнекороб", callback_data='general_firebox')],
        [InlineKeyboardButton("Просмотр пересечения", callback_data='general_intersection')],
        [InlineKeyboardButton("Менеджер узлов", callback_data='general_node_manager')],
        [InlineKeyboardButton("Просмотр пересечения", callback_data='general_model_check')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_general_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Этажи и секции", callback_data='general_floors')],
        [InlineKeyboardButton("Подсчет узлов", callback_data='general_nodes')],
        [InlineKeyboardButton("Печать листов", callback_data='general_print')],
        [InlineKeyboardButton("Множественная печать", callback_data='general_multiplie_print')],
        [InlineKeyboardButton("Копировать спецификацию", callback_data='general_copy_spec')],
        [InlineKeyboardButton("Копировать параметры", callback_data='general_copy_params')],
        [InlineKeyboardButton("Параметры семейств", callback_data='general_params')],
        [InlineKeyboardButton("Копировать параметры арматуры", callback_data='general_copy_params_armature')],
        [InlineKeyboardButton("Комбинатор дверей", callback_data='general_doors')],
        [InlineKeyboardButton("Огнекороб", callback_data='general_firebox')],
        [InlineKeyboardButton("Просмотр пересечения", callback_data='general_intersection')],
        [InlineKeyboardButton("Менеджер узлов", callback_data='general_node_manager')],
        [InlineKeyboardButton("Просмотр пересечения", callback_data='general_model_check')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_boxes_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Создание заданий", callback_data='boxes_tasks')],
        [InlineKeyboardButton("Объединение", callback_data='boxes_merge')],
        [InlineKeyboardButton("Смещение", callback_data='boxes_offset')],
        [InlineKeyboardButton("Обрезать", callback_data='boxes_cut')],
        [InlineKeyboardButton("Нумерация", callback_data='boxes_numbering')],
        [InlineKeyboardButton("Отметка", callback_data='boxes_mark')],
        [InlineKeyboardButton("Отверстия", callback_data='boxes_holes')],
        [InlineKeyboardButton("Проверка пересечений", callback_data='boxes_intersection_check')],
        [InlineKeyboardButton("Проверка пересекающихся заданий", callback_data='boxes_overlapping_tasks_check')],
        [InlineKeyboardButton("Статусы заданий", callback_data='boxes_tasks_status')],
        [InlineKeyboardButton("Обозреватель статусов", callback_data='boxes_status_observer')],
        [InlineKeyboardButton("Проверка заданий", callback_data='boxes_tasks_check')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_boxes_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Создание заданий", callback_data='boxes_tasks')],
        [InlineKeyboardButton("Объединение", callback_data='boxes_merge')],
        [InlineKeyboardButton("Смещение", callback_data='boxes_offset')],
        [InlineKeyboardButton("Обрезать", callback_data='boxes_cut')],
        [InlineKeyboardButton("Нумерация", callback_data='boxes_numbering')],
        [InlineKeyboardButton("Отметка", callback_data='boxes_mark')],
        [InlineKeyboardButton("Отверстия", callback_data='boxes_holes')],
        [InlineKeyboardButton("Проверка пересечений", callback_data='boxes_intersection_check')],
        [InlineKeyboardButton("Проверка пересекающихся заданий", callback_data='boxes_overlapping_tasks_check')],
        [InlineKeyboardButton("Статусы заданий", callback_data='boxes_tasks_status')],
        [InlineKeyboardButton("Обозреватель статусов", callback_data='boxes_status_observer')],
        [InlineKeyboardButton("Проверка заданий", callback_data='boxes_tasks_check')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_renga_plugin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [   
        [InlineKeyboardButton("Подсчет площадей", callback_data='renga_area')],
        [InlineKeyboardButton("Активация", callback_data='renga_activation')],
        [InlineKeyboardButton("Назад", callback_data='plugin_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("С каким плагином у вас возникла проблема:", reply_markup=reply_markup)

async def menu_renga_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Подсчет площадей", callback_data='renga_area')],
        [InlineKeyboardButton("Активация", callback_data='renga_activation')],
        [InlineKeyboardButton("Назад", callback_data='error_report')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("С каким плагином у вас возникла проблема:", reply_markup=reply_markup)

async def choose_revit_version_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Revit 2019", callback_data='revit_2019_help')],
        [InlineKeyboardButton("Revit 2020", callback_data='revit_2020_help')],
        [InlineKeyboardButton("Revit 2021", callback_data='revit_2021_help')],
        [InlineKeyboardButton("Revit 2022", callback_data='revit_2022_help')],
        [InlineKeyboardButton("Revit 2023", callback_data='revit_2023_help')],
        [InlineKeyboardButton("Revit 2024", callback_data='revit_2024_help')],
        [InlineKeyboardButton("Revit 2025", callback_data='revit_2025_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите версию Revit, в котором запускали плагин:", reply_markup=reply_markup)

async def ask_license_key_and_build_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("Введите, пожалуйста, ваш лицензионный ключ, который вы использовали.")
    context.user_data['stage'] = 'license_key'

async def handle_license_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'license_key':
        return

    context.user_data['license_key'] = update.message.text
    await update.message.reply_text("Напишите, пожалуйста, номер сборки, которую вы установили.")
    context.user_data['stage'] = 'build_number'

async def handle_build_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'build_number':
        return

    context.user_data['build_number'] = update.message.text
    if context.user_data.get('initial_choice') == 'error_report':
        await update.message.reply_text("Отправьте, пожалуйста, скриншот ошибки")
        context.user_data['stage'] = 'screenshot_and_description'
    elif context.user_data.get('initial_choice') == 'activation_help':
        await update.message.reply_text("Отправьте, пожалуйста, скриншот ошибки и опишите вашу проблему")
        context.user_data['stage'] = 'screenshot_and_description_activation'
    else:
        await update.message.reply_text("Опишите ваш вопрос.")
        context.user_data['stage'] = 'question_description'

async def handle_screenshot_and_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data:
        return

    if context.user_data['stage'] in ['screenshot_and_description', 'build_number_renga']:
        if update.message.photo:
            keyboard = [
                [InlineKeyboardButton("Не отправлять файл", callback_data='no_file')],
                [InlineKeyboardButton("Отправить файл", callback_data='send_file')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Отправьте, пожалуйста, файл на котором вышла данная ошибка, чтобы мы смогли изучить данную проблему.", reply_markup=reply_markup)
        else:
            await update.message.reply_text("Пожалуйста, отправьте скриншот ошибки.")
    elif context.user_data['stage'] == 'screenshot_and_description_activation':
        if update.message.photo:
            await update.message.reply_text("Данная ошибка была передана отделу разработок, в ближайшее время с вами свяжется специалист.")
            context.user_data.clear()
        else:
            await update.message.reply_text("Пожалуйста, отправьте скриншот ошибки и опишите вашу проблему.")

async def handle_screenshot_and_description_activation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'screenshot_and_description_activation':
        return

    if update.message.photo:
        await update.message.reply_text("Данная ошибка была передана отделу разработок, в ближайшее время с вами свяжется специалист.")
        context.user_data.clear()
    else:
        await update.message.reply_text("Пожалуйста, отправьте скриншот ошибки и опишите вашу проблему.")

async def handle_question_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'question_description':
        return

    keyboard = [
        [InlineKeyboardButton("Не отправлять файл", callback_data='no_file')],
        [InlineKeyboardButton("Отправить файл", callback_data='send_file')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Отправьте, пожалуйста, файл на котором у вас возник вопрос.", reply_markup=reply_markup)

async def handle_file_decision(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'no_file':
        await query.edit_message_text("Данный вопрос был передан отделу разработок, в ближайшее время с вами свяжется специалист.")
        context.user_data.clear()
    elif query.data == 'send_file':
        await query.edit_message_text("Прикрепите файл сюда.")
        context.user_data['stage'] = 'awaiting_file'

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'awaiting_file':
        return

    if update.message.document:
        await update.message.reply_text("Данный вопрос был передан отделу разработок, в ближайшее время с вами свяжется специалист.")
        context.user_data.clear()
    else:
        await update.message.reply_text("Пожалуйста, прикрепите файл.")

async def handle_file_after_screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'awaiting_file_after_screenshot':
        return

    if update.message.document:
        await update.message.reply_text("Данная ошибка была передана отделу разработок, в ближайшее время с вами свяжется специалист.")
        context.user_data.clear()
    else:
        await update.message.reply_text("Пожалуйста, прикрепите файл.")

async def ask_license_key_renga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("Введите лицензионный ключ, который у вас есть.")
    context.user_data['stage'] = 'license_key_renga'

async def handle_license_key_renga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'license_key_renga':
        return

    context.user_data['license_key'] = update.message.text
    await update.message.reply_text("Напишите версию Renga, в которой вы работаете.")
    context.user_data['stage'] = 'renga_version'

async def handle_renga_version(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'renga_version':
        return

    context.user_data['renga_version'] = update.message.text
    await update.message.reply_text("Напишите номер сборки плагинов, которую вы использовали.")
    context.user_data['stage'] = 'build_number_renga'

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' in context.user_data:
        if context.user_data['stage'] == 'license_key':
            await handle_license_key(update, context)
        elif context.user_data['stage'] == 'build_number':
            await handle_build_number(update, context)
        elif context.user_data['stage'] == 'screenshot_and_description':
            await handle_screenshot_and_description(update, context)
        elif context.user_data['stage'] == 'screenshot_and_description_activation':
            await handle_screenshot_and_description(update, context)
        elif context.user_data['stage'] == 'question_description':
            await handle_question_description(update, context)
        elif context.user_data['stage'] == 'license_key_renga':
            await handle_license_key_renga(update, context)
        elif context.user_data['stage'] == 'renga_version':
            await handle_renga_version(update, context)
        elif context.user_data['stage'] == 'build_number_renga':
            await handle_screenshot_and_description(update, context)  


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'menu_help':
        await menu_help(update, context)
    elif query.data == 'plugin_help':
        await plugin_help(update, context)
    elif query.data == 'error_report':
        context.user_data['initial_choice'] = 'error_report'
        await error_report(update, context)
    elif query.data == 'menu_concept_plugin':
        await menu_concept_plugin(update, context)
    elif query.data == 'menu_concept_error':
        await menu_concept_error(update, context)
    elif query.data == 'menu_architect_plugin':
        await menu_architect_plugin(update, context)
    elif query.data == 'menu_architect_error':
        await menu_architect_error(update, context)
    elif query.data == 'menu_constructive_plugin':
        await menu_constructive_plugin(update, context)
    elif query.data == 'menu_constructive_error':
        await menu_constructive_error(update, context)
    elif query.data == 'menu_ov_vk_plugin':
        await menu_ov_vk_plugin(update, context)
    elif query.data == 'menu_ov_vk_error':
        await menu_ov_vk_error(update, context)
    elif query.data == 'menu_general_plugin':
        await menu_general_plugin(update, context)
    elif query.data == 'menu_general_error':
        await menu_general_error(update, context)
    elif query.data == 'menu_boxes_plugin':
        await menu_boxes_plugin(update, context)
    elif query.data == 'menu_boxes_error':
        await menu_boxes_error(update, context)
    elif query.data == 'menu_renga_plugin':
        await menu_renga_plugin(update, context)
    elif query.data == 'menu_renga_error':
        await menu_renga_error(update, context)
    elif query.data == 'activation_help':
        context.user_data['initial_choice'] = 'activation_help'
        await activation_help(update, context)
    elif query.data in ['installation_error', 'registration_error', 'activation_key_error']:
        await choose_revit_version_help(update, context)
    elif query.data in ['revit_2019_help', 'revit_2020_help', 'revit_2021_help', 'revit_2022_help', 'revit_2023_help', 'revit_2024_help', 'revit_2025_help']:
        await ask_license_key_and_build_number(update, context)
    elif query.data in ['no_file', 'send_file']:
        await handle_file_decision(update, context)
    elif query.data in ['concept_insolation', 'concept_keo', 'concept_parks', 'concept_trees', 'concept_model', 'concept_3d', 'concept_tep', 'concept_areas',
                         'architect_room', 'architect_baseboard', 'architect_finishing', 'architect_copy', 'architect_openings', 'architect_floors', 'architect_areas',
                         'architect_planning', 'architect_round', 'architect_apartment', 'constructive_assembly', 'constructive_sections', 'constructive_plans',
                         'constructive_contour', 'constructive_contour_redactor', 'constructive_squeezing', 'constructive_frames', 'constructive_frametypes',
                         'ov_vk_couplings', 'ov_vk_aero', 'ov_vk_systemtypes', 'ov_vk_systems', 'ov_vk_elevations', 'ov_vk_wall_thickness', 'ov_vk_isolation', 'ov_vk_S_isolation',
                         'general_floors', 'general_nodes', 'general_print', 'general_multiplie_print', 'general_copy_spec', 'general_copy_params', 'general_params',
                         'general_copy_params_armature', 'general_doors', 'general_firebox', 'general_intersection', 'general_node_manager', 'general_model_check',
                         'boxes_tasks', 'boxes_merge', 'boxes_offset', 'boxes_cut', 'boxes_numbering', 'boxes_mark', 'boxes_holes', 'boxes_intersection_check',
                         'boxes_overlapping_tasks_check', 'boxes_tasks_status', 'boxes_status_observer', 'boxes_tasks_check']:
        await choose_revit_version_help(update, context)
    elif query.data in ['renga_area', 'renga_activation']:
        await ask_license_key_renga(update, context)
    elif query.data in ['renga_error_report', 'renga_question']:
        await handle_screenshot_and_description(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    application.add_handler(MessageHandler(filters.PHOTO, handle_screenshot_and_description))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file_after_screenshot))

    application.run_polling()

if __name__ == '__main__':
    main()
