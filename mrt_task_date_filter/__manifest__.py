# -*- coding: utf-8 -*-
{
    'name': 'Tasks Date Filter',
    'version': '12.0.1.0.0',
    'category': 'Project',
    'sequence': 1,
    'summary': "Tasks Deadline Date Filter",
    'description': "Module which adds new filters to Project Tasks",
    'author': 'Tiago Magrini Rigo',
    'website': '',
    'depends': ['base','project'],
    'data': [
        'views/project_views.xml'
    ],
    'images':['static/description/task_date_filter_cover.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': [],
}
