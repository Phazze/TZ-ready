from django import template
from ..models import Menu


register = template.Library()


@register.inclusion_tag('menu/dop.html', takes_context=True)
def draw_menu(context, menu):
    try:
        name_menu = Menu.objects.filter(menu__title=menu)
        name_menu_values = name_menu.values()
        primary_menu = [level for level in name_menu_values.filter(parent=None)]
        selected_menu_id = int(context['request'].GET[menu])
        selected_menu = name_menu.get(id=selected_menu_id)
        selected_menu_id_list = get_selected_item_id_list(selected_menu, primary_menu, selected_menu_id)

        for level in primary_menu:
            if level['id'] in selected_menu_id_list:
                level['child_levels'] = get_child_level(name_menu_values, level['id'], selected_menu_id_list)
        result_dict = {'name_menu': primary_menu}

    except:
        result_dict = {
            "name_menu": [
                level for level in Menu.objects.filter(menu__title=menu, parent=None).values()
            ]
        }
    result_dict['menu'] = menu
    return result_dict


# Функция для определения дочерних меню
def get_child_level(name_menu_values, current_level_id, selected_menu_id_list):
    level_list = [level for level in name_menu_values.filter(parent_id=current_level_id)]
    for level in level_list:
        if level['id'] in selected_menu_id_list:
            level['child_levels'] = get_child_level(name_menu_values, level['id'], selected_menu_id_list)
    return level_list


# Функция для определения выбранного каталога
def get_selected_item_id_list(parent, primary_menu, selected_menu_id):
    selected_menu_id_list = []

    while parent:
        selected_menu_id_list.append(parent.id)
        parent = parent.parent
        if not selected_menu_id_list:
            for level in primary_menu:
                if level['id'] == selected_menu_id:
                    selected_menu_id_list.append(selected_menu_id)

    return selected_menu_id_list
