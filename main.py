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
        [InlineKeyboardButton("Общее", callback_data='menu_general_error')],
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
        [InlineKeyboardButton("Отделка", callback_data='carchitect_finishing')],
        [InlineKeyboardButton("Копировать отделку", callback_data='architect_copy')],
        [InlineKeyboardButton("Проемы по дверям/окнам из связи", callback_data='architect_openings')],
        [InlineKeyboardButton("Соединение полов", callback_data='architect_floors')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='architect_areas')],
        [InlineKeyboardButton("Планировка", callback_data='architect_planning')],
        [InlineKeyboardButton("Округление площади", callback_data='architect_round')],
        [InlineKeyboardButton("Нумерация кваритр", callback_data='architect_apartment')],
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
        [InlineKeyboardButton("Отделка", callback_data='carchitect_finishing')],
        [InlineKeyboardButton("Копировать отделку", callback_data='architect_copy')],
        [InlineKeyboardButton("Проемы по дверям/окнам из связи", callback_data='architect_openings')],
        [InlineKeyboardButton("Соединение полов", callback_data='architect_floors')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='architect_areas')],
        [InlineKeyboardButton("Планировка", callback_data='architect_planning')],
        [InlineKeyboardButton("Округление площади", callback_data='architect_round')],
        [InlineKeyboardButton("Нумерация кваритр", callback_data='architect_apartment')],
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

async def choose_revit_version(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Revit 2019", callback_data='revit_2019')],
        [InlineKeyboardButton("Revit 2020", callback_data='revit_2020')],
        [InlineKeyboardButton("Revit 2021", callback_data='revit_2021')],
        [InlineKeyboardButton("Revit 2022", callback_data='revit_2022')],
        [InlineKeyboardButton("Revit 2023", callback_data='revit_2023')],
        [InlineKeyboardButton("Revit 2024", callback_data='revit_2024')],
        [InlineKeyboardButton("Revit 2025", callback_data='revit_2025')],
        [InlineKeyboardButton("Назад", callback_data='activation_help')]
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
    
    await update.message.reply_text("Теперь напишите, пожалуйста, номер сборки, которую вы установили.")
    context.user_data['stage'] = 'build_number'

async def handle_build_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'build_number':
        return
    
    context.user_data['build_number'] = update.message.text
    
    await update.message.reply_text("Отправьте, пожалуйста, скриншот ошибки и опишите вашу проблему.")
    context.user_data['stage'] = 'screenshot_and_description'

async def handle_screenshot_and_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' not in context.user_data or context.user_data['stage'] != 'screenshot_and_description':
        return
    
    if update.message.photo:
        await update.message.reply_text("Данная ошибка была передана отделу разработок, в ближайшее время с вами свяжется специалист.")
        context.user_data.clear()
    else:
        await update.message.reply_text("Пожалуйста, отправьте скриншот ошибки.")

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'stage' in context.user_data:
        if context.user_data['stage'] == 'license_key':
            await handle_license_key(update, context)
        elif context.user_data['stage'] == 'build_number':
            await handle_build_number(update, context)
        elif context.user_data['stage'] == 'screenshot_and_description':
            await handle_screenshot_and_description(update, context)

#async def menu_renga(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'menu_help':
        await menu_help(update, context)
    elif query.data == 'plugin_help':
        await plugin_help(update, context)
    elif query.data == 'error_report':
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
    elif query.data == 'activation_help':
        await activation_help(update, context)
    elif query.data in ['installation_error', 'registration_error', 'activation_key_error']:
        await choose_revit_version(update, context)
    elif query.data in ['revit_2019', 'revit_2020', 'revit_2021', 'revit_2022', 'revit_2023', 'revit_2024', 'revit_2025']:
        await ask_license_key_and_build_number(update, context)
    elif query.data == 'menu_renga':
        await menu_renga(update, context)
    elif query.data == 'back_to_start':
        await back_to_start(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    application.add_handler(MessageHandler(filters.PHOTO, handle_screenshot_and_description))

    application.run_polling()

if __name__ == '__main__':
    main()
