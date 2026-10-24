class Loc:
    widget_time_at_work = "//p[text()='Time at Work']"
    widget_my_actions = "//p[text()='My Actions']"
    widget_quick_launch = "//p[text()='Quick Launch']"
    widget_employee_distribution = "//p[text()='Employee Distribution by Sub Unit']"

    sidebar_search = "//input[@placeholder='Search']"
    sidebar_menu_items = "//a[contains(@class,'oxd-main-menu-item')]"
    page_header = "//h6[contains(@class,'oxd-topbar-header-breadcrumb-module')]"

    @staticmethod
    def sidebar_menu(name):
        return f"//a[contains(@class,'oxd-main-menu-item')][.//span[text()='{name}']]"