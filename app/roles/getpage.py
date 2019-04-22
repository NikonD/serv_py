def manage_persons_page(privileges):
    return {
        0:'roles/admin/main.html',
        1:'roles/head_teacher/main.html',
        2:'roles/methodist/main.html'
    }[privileges]
