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

async def menu_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Хочу задать вопрос касаемо работы плагина", callback_data='plugin_help')],
        [InlineKeyboardButton("Хочу сообщить об ошибке", callback_data='error_report')],
        [InlineKeyboardButton("Нужна помощь при установке/активации", callback_data='activation_help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите пункт, по которому вам нужна помощь:", reply_markup=reply_markup)

async def plugin_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Концепция", callback_data='menu_concept')],
        [InlineKeyboardButton("Отделка", callback_data='menu_otdelka')],
        [InlineKeyboardButton("Конструктив", callback_data='menu_constructive')],
        [InlineKeyboardButton("ОВ и ВК", callback_data='menu_ov_vk')],
        [InlineKeyboardButton("Общие", callback_data='menu_general')],
        [InlineKeyboardButton("Боксы и отверстия", callback_data='menu_boxes')],
        [InlineKeyboardButton("Renga", callback_data='menu_renga')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите из какой категории плагин, с которым вам нужна помощь:", reply_markup=reply_markup)

async def error_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Концепция", callback_data='menu_concept')],
        [InlineKeyboardButton("Архитектура", callback_data='menu_architect')],
        [InlineKeyboardButton("Конструктив", callback_data='menu_constructive')],
        [InlineKeyboardButton("ОВ и ВК", callback_data='menu_ov_vk')],
        [InlineKeyboardButton("Общее", callback_data='menu_general')],
        [InlineKeyboardButton("Боксы и отверстия", callback_data='menu_boxes')],
        [InlineKeyboardButton("Renga", callback_data='menu_renga')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите из какой категории плагин, с которым вам нужна помощь:", reply_markup=reply_markup)

async def menu_concept(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Инсоляция", callback_data='concept_insolation')],
        [InlineKeyboardButton("КЕО", callback_data='concept_keo')],
        [InlineKeyboardButton("Генерация деревьев", callback_data='concept_trees')],
        [InlineKeyboardButton("Разлиновка модели", callback_data='concept_model')],
        [InlineKeyboardButton("3D сетки", callback_data='concept_3d')],
        [InlineKeyboardButton("БыстроТЭПы", callback_data='concept_tep')],
        [InlineKeyboardButton("Подсчет площадей", callback_data='concept_areas')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_architect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        [InlineKeyboardButton("Нумерация кваритр", callback_data='architect_apartment')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_constructive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Сборка арматуры", callback_data='constructive_assembly')],
        [InlineKeyboardButton("Создать разрезы и сечения", callback_data='constructive_sections')],
        [InlineKeyboardButton("Создание планов", callback_data='constructive_plans')],
        [InlineKeyboardButton("Создание контура", callback_data='constructive_contour')],
        [InlineKeyboardButton("Редактирование контура", callback_data='constructive_contour_redactor')],
        [InlineKeyboardButton("Расчет продавливания", callback_data='constructive_squeezing')],
        [InlineKeyboardButton("Создание каркасов", callback_data='constructive_frames')],
        [InlineKeyboardButton("Создание видов каркасов", callback_data='constructive_frametypes')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_ov_vk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Муфты/гильзы", callback_data='ov_vk_couplings')],
        [InlineKeyboardButton("Аэродинамика", callback_data='ov_vk_aero')],
        [InlineKeyboardButton("Создать виды систем", callback_data='ov_vk_systemtypes')],
        [InlineKeyboardButton("Спецификации систем", callback_data='ov_vk_systems')],
        [InlineKeyboardButton("Высотные отметки", callback_data='ov_vk_elevations')],
        [InlineKeyboardButton("Толщина стенки", callback_data='ov_vk_wall_thickness')],
        [InlineKeyboardButton("Диаметр изоляции", callback_data='ov_vk_isolation')],
        [InlineKeyboardButton("S изоляции", callback_data='ov_vk_S_isolation')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_general(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        [InlineKeyboardButton("Просмотр пересечения", callback_data='general_model_check')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

async def menu_boxes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
        [InlineKeyboardButton("Проверка заданий", callback_data='boxes_tasks_check')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Выберите каким плагином вы воспользовались:", reply_markup=reply_markup)

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
    elif query.data == 'menu_concept':
        await menu_concept(update, context)
    elif query.data == 'menu_architect':
        await menu_architect(update, context)
    elif query.data == 'menu_constructive':
        await menu_constructive(update, context)
    elif query.data == 'menu_ov_vk':
        await menu_ov_vk(update, context)
    elif query.data == 'menu_general':
        await menu_general(update, context)
    elif query.data == 'menu_boxes':
        await menu_boxes(update, context)
    elif query.data == 'menu_renga':
        await menu_renga(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()
