from pom.components.base_page import BasePage, GLOBAL_TIMEOUT
from resources import locators_manager


LOCATORS = locators_manager.get_locators("main_menu")


class MainMenu(BasePage):
    def __init__(self, driver, debug=False):
        super().__init__(driver, debug)

    ADMIN_MAIN_MENU = LOCATORS.get("ADMIN").get("MAIN_MENU")
    ADMIN_USER_MANAGEMENT_MAIN_MENU = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("MAIN_MENU")
    ADMIN_USER_MANAGEMENT_USERS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("USERS")
    ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("OPTIONAL_FIELDS")
    ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("CUSTOM_FIELDS")
    ADMIN_USER_MANAGEMENT_DATA_IMPORT = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("DATA_IMPORT")
    ADMIN_USER_MANAGEMENT_REPORTING_METHODS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("REPORTING_METHODS")
    ADMIN_USER_MANAGEMENT_TERMINATION_REASONS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("TERMINATION_REASONS")
    ADMIN_USER_MANAGEMENT_MY_TIMESHEETS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("MY_TIMESHEETS")
    ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("EMPLOYEE_TIMESHEETS")
    ADMIN_USER_MANAGEMENT_KPIS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("KPIS")
    ADMIN_USER_MANAGEMENT_TRACKERS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("TRACKERS")
    ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("EMPLOYEE_RECORDS")
    ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS = LOCATORS.get("ADMIN").get("USER_MANAGEMENT").get("CANDIDATE_RECORDS")
    ADMIN_JOB_MAIN_MENU = LOCATORS.get("ADMIN").get("JOB").get("MAIN_MENU")
    ADMIN_JOB_JOB_TITLES = LOCATORS.get("ADMIN").get("JOB").get("JOB_TITLES")
    ADMIN_JOB_PAY_GRADES = LOCATORS.get("ADMIN").get("JOB").get("PAY_GRADES")
    ADMIN_JOB_EMPLOYMENT_STATUS = LOCATORS.get("ADMIN").get("JOB").get("EMPLOYMENT_STATUS")
    ADMIN_JOB_JOB_CATEGORIES = LOCATORS.get("ADMIN").get("JOB").get("JOB_CATEGORIES")
    ADMIN_JOB_WORK_SHIFTS = LOCATORS.get("ADMIN").get("JOB").get("WORK_SHIFTS")
    ADMIN_JOB_MY_RECORDS = LOCATORS.get("ADMIN").get("JOB").get("MY_RECORDS")
    ADMIN_JOB_PUNCH_IN_OUT = LOCATORS.get("ADMIN").get("JOB").get("PUNCH_IN_OUT")
    ADMIN_JOB_EMPLOYEE_RECORDS = LOCATORS.get("ADMIN").get("JOB").get("EMPLOYEE_RECORDS")
    ADMIN_JOB_CONFIGURATION = LOCATORS.get("ADMIN").get("JOB").get("CONFIGURATION")
    ADMIN_JOB_MANAGE_REVIEWS = LOCATORS.get("ADMIN").get("JOB").get("MANAGE_REVIEWS")
    ADMIN_JOB_MY_REVIEWS = LOCATORS.get("ADMIN").get("JOB").get("MY_REVIEWS")
    ADMIN_JOB_REVIEW_LIST = LOCATORS.get("ADMIN").get("JOB").get("REVIEW_LIST")
    ADMIN_ORGANIZATION_MAIN_MENU = LOCATORS.get("ADMIN").get("ORGANIZATION").get("MAIN_MENU")
    ADMIN_ORGANIZATION_GENERAL_INFORMATION = LOCATORS.get("ADMIN").get("ORGANIZATION").get("GENERAL_INFORMATION")
    ADMIN_ORGANIZATION_LOCATIONS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("LOCATIONS")
    ADMIN_ORGANIZATION_STRUCTURE = LOCATORS.get("ADMIN").get("ORGANIZATION").get("STRUCTURE")
    ADMIN_ORGANIZATION_ADD_ENTITLEMENTS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("ADD_ENTITLEMENTS")
    ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("EMPLOYEE_ENTITLEMENTS")
    ADMIN_ORGANIZATION_MY_ENTITLEMENTS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("MY_ENTITLEMENTS")
    ADMIN_ORGANIZATION_PROJECT_REPORTS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("PROJECT_REPORTS")
    ADMIN_ORGANIZATION_EMPLOYEE_REPORTS = LOCATORS.get("ADMIN").get("ORGANIZATION").get("EMPLOYEE_REPORTS")
    ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY = LOCATORS.get("ADMIN").get("ORGANIZATION").get("ATTENDANCE_SUMMARY")
    ADMIN_QUALIFICATIONS_MAIN_MENU = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("MAIN_MENU")
    ADMIN_QUALIFICATIONS_SKILLS = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("SKILLS")
    ADMIN_QUALIFICATIONS_EDUCATION = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("EDUCATION")
    ADMIN_QUALIFICATIONS_LICENSES = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("LICENSES")
    ADMIN_QUALIFICATIONS_LANGUAGES = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("LANGUAGES")
    ADMIN_QUALIFICATIONS_MEMBERSHIPS = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("MEMBERSHIPS")
    ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT = (
        LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("LEAVE_ENTITLEMENTS_AND_USAGE_REPORT")
    )
    ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT = (
        LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT")
    )
    ADMIN_QUALIFICATIONS_CUSTOMERS = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("CUSTOMERS")
    ADMIN_QUALIFICATIONS_PROJECTS = LOCATORS.get("ADMIN").get("QUALIFICATIONS").get("PROJECTS")
    ADMIN_NATIONALITIES_MAIN_MENU = LOCATORS.get("ADMIN").get("NATIONALITIES").get("MAIN_MENU")
    ADMIN_NATIONALITIES_LEAVE_PERIOD = LOCATORS.get("ADMIN").get("NATIONALITIES").get("LEAVE_PERIOD")
    ADMIN_NATIONALITIES_LEAVE_TYPES = LOCATORS.get("ADMIN").get("NATIONALITIES").get("LEAVE_TYPES")
    ADMIN_NATIONALITIES_WORK_WEEK = LOCATORS.get("ADMIN").get("NATIONALITIES").get("WORK_WEEK")
    ADMIN_NATIONALITIES_HOLIDAYS = LOCATORS.get("ADMIN").get("NATIONALITIES").get("HOLIDAYS")
    ADMIN_CORPORATE_BRANDING_MAIN_MENU = LOCATORS.get("ADMIN").get("CORPORATE_BRANDING").get("MAIN_MENU")
    ADMIN_CONFIGURATION_MAIN_MENU = LOCATORS.get("ADMIN").get("CONFIGURATION").get("MAIN_MENU")
    ADMIN_CONFIGURATION_EMAIL_CONFIGURATION = LOCATORS.get("ADMIN").get("CONFIGURATION").get("EMAIL_CONFIGURATION")
    ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS = LOCATORS.get("ADMIN").get("CONFIGURATION").get("EMAIL_SUBSCRIPTIONS")
    ADMIN_CONFIGURATION_LOCALIZATION = LOCATORS.get("ADMIN").get("CONFIGURATION").get("LOCALIZATION")
    ADMIN_CONFIGURATION_LANGUAGE_PACKAGES = LOCATORS.get("ADMIN").get("CONFIGURATION").get("LANGUAGE_PACKAGES")
    ADMIN_CONFIGURATION_MODULES = LOCATORS.get("ADMIN").get("CONFIGURATION").get("MODULES")
    ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION = (
        LOCATORS.get("ADMIN").get("CONFIGURATION").get("SOCIAL_MEDIA_AUTHENTICATION")
    )
    ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT = LOCATORS.get("ADMIN").get("CONFIGURATION").get("REGISTER_OAUTH_CLIENT")
    PIM_MAIN_MENU = LOCATORS.get("PIM").get("MAIN_MENU")
    PIM_CONFIGURATION_MAIN_MENU = LOCATORS.get("PIM").get("CONFIGURATION").get("MAIN_MENU")
    PIM_CONFIGURATION_OPTIONAL_FIELDS = LOCATORS.get("PIM").get("CONFIGURATION").get("OPTIONAL_FIELDS")
    PIM_CONFIGURATION_CUSTOM_FIELDS = LOCATORS.get("PIM").get("CONFIGURATION").get("CUSTOM_FIELDS")
    PIM_CONFIGURATION_DATA_IMPORT = LOCATORS.get("PIM").get("CONFIGURATION").get("DATA_IMPORT")
    PIM_CONFIGURATION_REPORTING_METHODS = LOCATORS.get("PIM").get("CONFIGURATION").get("REPORTING_METHODS")
    PIM_CONFIGURATION_TERMINATION_REASONS = LOCATORS.get("PIM").get("CONFIGURATION").get("TERMINATION_REASONS")
    PIM_EMPLOYEE_LIST_MAIN_MENU = LOCATORS.get("PIM").get("EMPLOYEE_LIST").get("MAIN_MENU")
    PIM_ADD_EMPLOYEE_MAIN_MENU = LOCATORS.get("PIM").get("ADD_EMPLOYEE").get("MAIN_MENU")
    PIM_REPORTS_MAIN_MENU = LOCATORS.get("PIM").get("REPORTS").get("MAIN_MENU")
    LEAVE_MAIN_MENU = LOCATORS.get("LEAVE").get("MAIN_MENU")
    LEAVE_APPLY_MAIN_MENU = LOCATORS.get("LEAVE").get("APPLY").get("MAIN_MENU")
    LEAVE_MY_LEAVE_MAIN_MENU = LOCATORS.get("LEAVE").get("MY_LEAVE").get("MAIN_MENU")
    LEAVE_ENTITLEMENTS_MAIN_MENU = LOCATORS.get("LEAVE").get("ENTITLEMENTS").get("MAIN_MENU")
    LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS = LOCATORS.get("LEAVE").get("ENTITLEMENTS").get("ADD_ENTITLEMENTS")
    LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS = LOCATORS.get("LEAVE").get("ENTITLEMENTS").get("EMPLOYEE_ENTITLEMENTS")
    LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS = LOCATORS.get("LEAVE").get("ENTITLEMENTS").get("MY_ENTITLEMENTS")
    LEAVE_REPORTS_MAIN_MENU = LOCATORS.get("LEAVE").get("REPORTS").get("MAIN_MENU")
    LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT = (
        LOCATORS.get("LEAVE").get("REPORTS").get("LEAVE_ENTITLEMENTS_AND_USAGE_REPORT")
    )
    LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT = (
        LOCATORS.get("LEAVE").get("REPORTS").get("MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT")
    )
    LEAVE_CONFIGURE_MAIN_MENU = LOCATORS.get("LEAVE").get("CONFIGURE").get("MAIN_MENU")
    LEAVE_CONFIGURE_LEAVE_PERIOD = LOCATORS.get("LEAVE").get("CONFIGURE").get("LEAVE_PERIOD")
    LEAVE_CONFIGURE_LEAVE_TYPES = LOCATORS.get("LEAVE").get("CONFIGURE").get("LEAVE_TYPES")
    LEAVE_CONFIGURE_WORK_WEEK = LOCATORS.get("LEAVE").get("CONFIGURE").get("WORK_WEEK")
    LEAVE_CONFIGURE_HOLIDAYS = LOCATORS.get("LEAVE").get("CONFIGURE").get("HOLIDAYS")
    LEAVE_LEAVE_LIST_MAIN_MENU = LOCATORS.get("LEAVE").get("LEAVE_LIST").get("MAIN_MENU")
    LEAVE_ASSIGN_LEAVE_MAIN_MENU = LOCATORS.get("LEAVE").get("ASSIGN_LEAVE").get("MAIN_MENU")
    TIME_MAIN_MENU = LOCATORS.get("TIME").get("MAIN_MENU")
    TIME_TIMESHEETS_MAIN_MENU = LOCATORS.get("TIME").get("TIMESHEETS").get("MAIN_MENU")
    TIME_TIMESHEETS_MY_TIMESHEETS = LOCATORS.get("TIME").get("TIMESHEETS").get("MY_TIMESHEETS")
    TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS = LOCATORS.get("TIME").get("TIMESHEETS").get("EMPLOYEE_TIMESHEETS")
    TIME_ATTENDANCE_MAIN_MENU = LOCATORS.get("TIME").get("ATTENDANCE").get("MAIN_MENU")
    TIME_ATTENDANCE_MY_RECORDS = LOCATORS.get("TIME").get("ATTENDANCE").get("MY_RECORDS")
    TIME_ATTENDANCE_PUNCH_IN_OUT = LOCATORS.get("TIME").get("ATTENDANCE").get("PUNCH_IN_OUT")
    TIME_ATTENDANCE_EMPLOYEE_RECORDS = LOCATORS.get("TIME").get("ATTENDANCE").get("EMPLOYEE_RECORDS")
    TIME_ATTENDANCE_CONFIGURATION = LOCATORS.get("TIME").get("ATTENDANCE").get("CONFIGURATION")
    TIME_REPORTS_MAIN_MENU = LOCATORS.get("TIME").get("REPORTS").get("MAIN_MENU")
    TIME_REPORTS_PROJECT_REPORTS = LOCATORS.get("TIME").get("REPORTS").get("PROJECT_REPORTS")
    TIME_REPORTS_EMPLOYEE_REPORTS = LOCATORS.get("TIME").get("REPORTS").get("EMPLOYEE_REPORTS")
    TIME_REPORTS_ATTENDANCE_SUMMARY = LOCATORS.get("TIME").get("REPORTS").get("ATTENDANCE_SUMMARY")
    TIME_PROJECT_INFO_MAIN_MENU = LOCATORS.get("TIME").get("PROJECT_INFO").get("MAIN_MENU")
    TIME_PROJECT_INFO_CUSTOMERS = LOCATORS.get("TIME").get("PROJECT_INFO").get("CUSTOMERS")
    TIME_PROJECT_INFO_PROJECTS = LOCATORS.get("TIME").get("PROJECT_INFO").get("PROJECTS")
    RECRUITMENT_MAIN_MENU = LOCATORS.get("RECRUITMENT").get("MAIN_MENU")
    RECRUITMENT_CANDIDATES_MAIN_MENU = LOCATORS.get("RECRUITMENT").get("CANDIDATES").get("MAIN_MENU")
    RECRUITMENT_VACANCIES_MAIN_MENU = LOCATORS.get("RECRUITMENT").get("VACANCIES").get("MAIN_MENU")
    MY_INFO_MAIN_MENU = LOCATORS.get("MY_INFO").get("MAIN_MENU")
    PERFORMANCE_MAIN_MENU = LOCATORS.get("PERFORMANCE").get("MAIN_MENU")
    PERFORMANCE_CONFIGURE_MAIN_MENU = LOCATORS.get("PERFORMANCE").get("CONFIGURE").get("MAIN_MENU")
    PERFORMANCE_CONFIGURE_KPIS = LOCATORS.get("PERFORMANCE").get("CONFIGURE").get("KPIS")
    PERFORMANCE_CONFIGURE_TRACKERS = LOCATORS.get("PERFORMANCE").get("CONFIGURE").get("TRACKERS")
    PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU = LOCATORS.get("PERFORMANCE").get("MANAGE_REVIEWS").get("MAIN_MENU")
    PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS = LOCATORS.get("PERFORMANCE").get("MANAGE_REVIEWS").get("MANAGE_REVIEWS")
    PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS = LOCATORS.get("PERFORMANCE").get("MANAGE_REVIEWS").get("MY_REVIEWS")
    PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST = LOCATORS.get("PERFORMANCE").get("MANAGE_REVIEWS").get("REVIEW_LIST")
    PERFORMANCE_MY_TRACKERS_MAIN_MENU = LOCATORS.get("PERFORMANCE").get("MY_TRACKERS").get("MAIN_MENU")
    PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU = LOCATORS.get("PERFORMANCE").get("EMPLOYEE_TRACKERS").get("MAIN_MENU")
    DASHBOARD_MAIN_MENU = LOCATORS.get("DASHBOARD").get("MAIN_MENU")
    DIRECTORY_MAIN_MENU = LOCATORS.get("DIRECTORY").get("MAIN_MENU")
    MAINTENANCE_MAIN_MENU = LOCATORS.get("MAINTENANCE").get("MAIN_MENU")
    MAINTENANCE_PURGE_RECORDS_MAIN_MENU = LOCATORS.get("MAINTENANCE").get("PURGE_RECORDS").get("MAIN_MENU")
    MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS = (
        LOCATORS.get("MAINTENANCE").get("PURGE_RECORDS").get("EMPLOYEE_RECORDS")
    )
    MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS = (
        LOCATORS.get("MAINTENANCE").get("PURGE_RECORDS").get("CANDIDATE_RECORDS")
    )
    MAINTENANCE_ACCESS_RECORDS_MAIN_MENU = LOCATORS.get("MAINTENANCE").get("ACCESS_RECORDS").get("MAIN_MENU")
    BUZZ_MAIN_MENU = LOCATORS.get("BUZZ").get("MAIN_MENU")

    def wait_until_page_contains_admin_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_user_management_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_user_management_users(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_USERS, timeout)

    def wait_until_page_contains_admin_user_management_optional_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS, timeout)

    def wait_until_page_contains_admin_user_management_custom_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS, timeout)

    def wait_until_page_contains_admin_user_management_data_import(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT, timeout)

    def wait_until_page_contains_admin_user_management_reporting_methods(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS, timeout)

    def wait_until_page_contains_admin_user_management_termination_reasons(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS, timeout)

    def wait_until_page_contains_admin_user_management_my_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS, timeout)

    def wait_until_page_contains_admin_user_management_employee_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_page_contains_admin_user_management_kpis(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_KPIS, timeout)

    def wait_until_page_contains_admin_user_management_trackers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_TRACKERS, timeout)

    def wait_until_page_contains_admin_user_management_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_contains_admin_user_management_candidate_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS, timeout)

    def wait_until_page_contains_admin_job_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_job_job_titles(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_JOB_TITLES, timeout)

    def wait_until_page_contains_admin_job_pay_grades(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_PAY_GRADES, timeout)

    def wait_until_page_contains_admin_job_employment_status(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_EMPLOYMENT_STATUS, timeout)

    def wait_until_page_contains_admin_job_job_categories(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_JOB_CATEGORIES, timeout)

    def wait_until_page_contains_admin_job_work_shifts(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_WORK_SHIFTS, timeout)

    def wait_until_page_contains_admin_job_my_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_MY_RECORDS, timeout)

    def wait_until_page_contains_admin_job_punch_in_out(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_PUNCH_IN_OUT, timeout)

    def wait_until_page_contains_admin_job_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_contains_admin_job_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_CONFIGURATION, timeout)

    def wait_until_page_contains_admin_job_manage_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_MANAGE_REVIEWS, timeout)

    def wait_until_page_contains_admin_job_my_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_MY_REVIEWS, timeout)

    def wait_until_page_contains_admin_job_review_list(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_JOB_REVIEW_LIST, timeout)

    def wait_until_page_contains_admin_organization_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_organization_general_information(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION, timeout)

    def wait_until_page_contains_admin_organization_locations(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_LOCATIONS, timeout)

    def wait_until_page_contains_admin_organization_structure(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_STRUCTURE, timeout)

    def wait_until_page_contains_admin_organization_add_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS, timeout)

    def wait_until_page_contains_admin_organization_employee_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_page_contains_admin_organization_my_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS, timeout)

    def wait_until_page_contains_admin_organization_project_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_PROJECT_REPORTS, timeout)

    def wait_until_page_contains_admin_organization_employee_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS, timeout)

    def wait_until_page_contains_admin_organization_attendance_summary(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY, timeout)

    def wait_until_page_contains_admin_qualifications_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_qualifications_skills(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_SKILLS, timeout)

    def wait_until_page_contains_admin_qualifications_education(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_EDUCATION, timeout)

    def wait_until_page_contains_admin_qualifications_licenses(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_LICENSES, timeout)

    def wait_until_page_contains_admin_qualifications_languages(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_LANGUAGES, timeout)

    def wait_until_page_contains_admin_qualifications_memberships(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS, timeout)

    def wait_until_page_contains_admin_qualifications_leave_entitlements_and_usage_report(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_page_contains_admin_qualifications_my_leave_entitlements_and_usage_report(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_page_contains_admin_qualifications_customers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_CUSTOMERS, timeout)

    def wait_until_page_contains_admin_qualifications_projects(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_QUALIFICATIONS_PROJECTS, timeout)

    def wait_until_page_contains_admin_nationalities_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_NATIONALITIES_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_nationalities_leave_period(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_NATIONALITIES_LEAVE_PERIOD, timeout)

    def wait_until_page_contains_admin_nationalities_leave_types(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_NATIONALITIES_LEAVE_TYPES, timeout)

    def wait_until_page_contains_admin_nationalities_work_week(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_NATIONALITIES_WORK_WEEK, timeout)

    def wait_until_page_contains_admin_nationalities_holidays(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_NATIONALITIES_HOLIDAYS, timeout)

    def wait_until_page_contains_admin_corporate_branding_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_configuration_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_page_contains_admin_configuration_email_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION, timeout)

    def wait_until_page_contains_admin_configuration_email_subscriptions(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS, timeout)

    def wait_until_page_contains_admin_configuration_localization(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_LOCALIZATION, timeout)

    def wait_until_page_contains_admin_configuration_language_packages(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES, timeout)

    def wait_until_page_contains_admin_configuration_modules(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_MODULES, timeout)

    def wait_until_page_contains_admin_configuration_social_media_authentication(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION, timeout)

    def wait_until_page_contains_admin_configuration_register_oauth_client(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT, timeout)

    def wait_until_page_contains_pim_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_MAIN_MENU, timeout)

    def wait_until_page_contains_pim_configuration_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_page_contains_pim_configuration_optional_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_OPTIONAL_FIELDS, timeout)

    def wait_until_page_contains_pim_configuration_custom_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_CUSTOM_FIELDS, timeout)

    def wait_until_page_contains_pim_configuration_data_import(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_DATA_IMPORT, timeout)

    def wait_until_page_contains_pim_configuration_reporting_methods(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_REPORTING_METHODS, timeout)

    def wait_until_page_contains_pim_configuration_termination_reasons(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_CONFIGURATION_TERMINATION_REASONS, timeout)

    def wait_until_page_contains_pim_employee_list_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_EMPLOYEE_LIST_MAIN_MENU, timeout)

    def wait_until_page_contains_pim_add_employee_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_ADD_EMPLOYEE_MAIN_MENU, timeout)

    def wait_until_page_contains_pim_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PIM_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_apply_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_APPLY_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_my_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_MY_LEAVE_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_entitlements_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_ENTITLEMENTS_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_entitlements_add_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS, timeout)

    def wait_until_page_contains_leave_entitlements_employee_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_page_contains_leave_entitlements_my_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS, timeout)

    def wait_until_page_contains_leave_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_reports_leave_entitlements_and_usage_report(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_page_contains_leave_reports_my_leave_entitlements_and_usage_report(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_page_contains_leave_configure_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_configure_leave_period(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_CONFIGURE_LEAVE_PERIOD, timeout)

    def wait_until_page_contains_leave_configure_leave_types(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_CONFIGURE_LEAVE_TYPES, timeout)

    def wait_until_page_contains_leave_configure_work_week(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_CONFIGURE_WORK_WEEK, timeout)

    def wait_until_page_contains_leave_configure_holidays(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_CONFIGURE_HOLIDAYS, timeout)

    def wait_until_page_contains_leave_leave_list_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_LEAVE_LIST_MAIN_MENU, timeout)

    def wait_until_page_contains_leave_assign_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU, timeout)

    def wait_until_page_contains_time_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_MAIN_MENU, timeout)

    def wait_until_page_contains_time_timesheets_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_TIMESHEETS_MAIN_MENU, timeout)

    def wait_until_page_contains_time_timesheets_my_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_TIMESHEETS_MY_TIMESHEETS, timeout)

    def wait_until_page_contains_time_timesheets_employee_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_page_contains_time_attendance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_ATTENDANCE_MAIN_MENU, timeout)

    def wait_until_page_contains_time_attendance_my_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_ATTENDANCE_MY_RECORDS, timeout)

    def wait_until_page_contains_time_attendance_punch_in_out(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_ATTENDANCE_PUNCH_IN_OUT, timeout)

    def wait_until_page_contains_time_attendance_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_contains_time_attendance_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_ATTENDANCE_CONFIGURATION, timeout)

    def wait_until_page_contains_time_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_contains_time_reports_project_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_REPORTS_PROJECT_REPORTS, timeout)

    def wait_until_page_contains_time_reports_employee_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_REPORTS_EMPLOYEE_REPORTS, timeout)

    def wait_until_page_contains_time_reports_attendance_summary(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_REPORTS_ATTENDANCE_SUMMARY, timeout)

    def wait_until_page_contains_time_project_info_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_PROJECT_INFO_MAIN_MENU, timeout)

    def wait_until_page_contains_time_project_info_customers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_PROJECT_INFO_CUSTOMERS, timeout)

    def wait_until_page_contains_time_project_info_projects(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.TIME_PROJECT_INFO_PROJECTS, timeout)

    def wait_until_page_contains_recruitment_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.RECRUITMENT_MAIN_MENU, timeout)

    def wait_until_page_contains_recruitment_candidates_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.RECRUITMENT_CANDIDATES_MAIN_MENU, timeout)

    def wait_until_page_contains_recruitment_vacancies_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.RECRUITMENT_VACANCIES_MAIN_MENU, timeout)

    def wait_until_page_contains_my_info_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MY_INFO_MAIN_MENU, timeout)

    def wait_until_page_contains_performance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MAIN_MENU, timeout)

    def wait_until_page_contains_performance_configure_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_page_contains_performance_configure_kpis(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_CONFIGURE_KPIS, timeout)

    def wait_until_page_contains_performance_configure_trackers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_CONFIGURE_TRACKERS, timeout)

    def wait_until_page_contains_performance_manage_reviews_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU, timeout)

    def wait_until_page_contains_performance_manage_reviews_manage_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS, timeout)

    def wait_until_page_contains_performance_manage_reviews_my_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS, timeout)

    def wait_until_page_contains_performance_manage_reviews_review_list(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST, timeout)

    def wait_until_page_contains_performance_my_trackers_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU, timeout)

    def wait_until_page_contains_performance_employee_trackers_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU, timeout)

    def wait_until_page_contains_dashboard_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.DASHBOARD_MAIN_MENU, timeout)

    def wait_until_page_contains_directory_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.DIRECTORY_MAIN_MENU, timeout)

    def wait_until_page_contains_maintenance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MAINTENANCE_MAIN_MENU, timeout)

    def wait_until_page_contains_maintenance_purge_records_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU, timeout)

    def wait_until_page_contains_maintenance_purge_records_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_contains_maintenance_purge_records_candidate_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS, timeout)

    def wait_until_page_contains_maintenance_access_records_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU, timeout)

    def wait_until_page_contains_buzz_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_contains_element(self.BUZZ_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_user_management_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_user_management_users(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_USERS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_optional_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_custom_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_data_import(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT, timeout)

    def wait_until_page_does_not_contain_admin_user_management_reporting_methods(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_termination_reasons(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_my_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_employee_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_kpis(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_KPIS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_trackers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_TRACKERS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_does_not_contain_admin_user_management_candidate_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS, timeout)

    def wait_until_page_does_not_contain_admin_job_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_job_job_titles(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_JOB_TITLES, timeout)

    def wait_until_page_does_not_contain_admin_job_pay_grades(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_PAY_GRADES, timeout)

    def wait_until_page_does_not_contain_admin_job_employment_status(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_EMPLOYMENT_STATUS, timeout)

    def wait_until_page_does_not_contain_admin_job_job_categories(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_JOB_CATEGORIES, timeout)

    def wait_until_page_does_not_contain_admin_job_work_shifts(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_WORK_SHIFTS, timeout)

    def wait_until_page_does_not_contain_admin_job_my_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_MY_RECORDS, timeout)

    def wait_until_page_does_not_contain_admin_job_punch_in_out(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_PUNCH_IN_OUT, timeout)

    def wait_until_page_does_not_contain_admin_job_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_does_not_contain_admin_job_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_CONFIGURATION, timeout)

    def wait_until_page_does_not_contain_admin_job_manage_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_MANAGE_REVIEWS, timeout)

    def wait_until_page_does_not_contain_admin_job_my_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_MY_REVIEWS, timeout)

    def wait_until_page_does_not_contain_admin_job_review_list(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_JOB_REVIEW_LIST, timeout)

    def wait_until_page_does_not_contain_admin_organization_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_organization_general_information(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION, timeout)

    def wait_until_page_does_not_contain_admin_organization_locations(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_LOCATIONS, timeout)

    def wait_until_page_does_not_contain_admin_organization_structure(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_STRUCTURE, timeout)

    def wait_until_page_does_not_contain_admin_organization_add_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_admin_organization_employee_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_admin_organization_my_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_admin_organization_project_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_PROJECT_REPORTS, timeout)

    def wait_until_page_does_not_contain_admin_organization_employee_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS, timeout)

    def wait_until_page_does_not_contain_admin_organization_attendance_summary(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_skills(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_SKILLS, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_education(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_EDUCATION, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_licenses(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_LICENSES, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_languages(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_LANGUAGES, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_memberships(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_leave_entitlements_and_usage_report(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_page_does_not_contains_element(
            self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout
        )

    def wait_until_page_does_not_contain_admin_qualifications_my_leave_entitlements_and_usage_report(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_page_does_not_contains_element(
            self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout
        )

    def wait_until_page_does_not_contain_admin_qualifications_customers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_CUSTOMERS, timeout)

    def wait_until_page_does_not_contain_admin_qualifications_projects(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_QUALIFICATIONS_PROJECTS, timeout)

    def wait_until_page_does_not_contain_admin_nationalities_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_NATIONALITIES_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_nationalities_leave_period(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_NATIONALITIES_LEAVE_PERIOD, timeout)

    def wait_until_page_does_not_contain_admin_nationalities_leave_types(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_NATIONALITIES_LEAVE_TYPES, timeout)

    def wait_until_page_does_not_contain_admin_nationalities_work_week(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_NATIONALITIES_WORK_WEEK, timeout)

    def wait_until_page_does_not_contain_admin_nationalities_holidays(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_NATIONALITIES_HOLIDAYS, timeout)

    def wait_until_page_does_not_contain_admin_corporate_branding_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_configuration_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_admin_configuration_email_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION, timeout)

    def wait_until_page_does_not_contain_admin_configuration_email_subscriptions(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS, timeout)

    def wait_until_page_does_not_contain_admin_configuration_localization(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_LOCALIZATION, timeout)

    def wait_until_page_does_not_contain_admin_configuration_language_packages(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES, timeout)

    def wait_until_page_does_not_contain_admin_configuration_modules(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_MODULES, timeout)

    def wait_until_page_does_not_contain_admin_configuration_social_media_authentication(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION, timeout)

    def wait_until_page_does_not_contain_admin_configuration_register_oauth_client(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT, timeout)

    def wait_until_page_does_not_contain_pim_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_pim_configuration_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_pim_configuration_optional_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_OPTIONAL_FIELDS, timeout)

    def wait_until_page_does_not_contain_pim_configuration_custom_fields(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_CUSTOM_FIELDS, timeout)

    def wait_until_page_does_not_contain_pim_configuration_data_import(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_DATA_IMPORT, timeout)

    def wait_until_page_does_not_contain_pim_configuration_reporting_methods(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_REPORTING_METHODS, timeout)

    def wait_until_page_does_not_contain_pim_configuration_termination_reasons(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_CONFIGURATION_TERMINATION_REASONS, timeout)

    def wait_until_page_does_not_contain_pim_employee_list_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_EMPLOYEE_LIST_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_pim_add_employee_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_ADD_EMPLOYEE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_pim_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PIM_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_apply_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_APPLY_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_my_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_MY_LEAVE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_entitlements_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_ENTITLEMENTS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_entitlements_add_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_leave_entitlements_employee_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_leave_entitlements_my_entitlements(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS, timeout)

    def wait_until_page_does_not_contain_leave_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_reports_leave_entitlements_and_usage_report(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_page_does_not_contains_element(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_page_does_not_contain_leave_reports_my_leave_entitlements_and_usage_report(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_page_does_not_contains_element(
            self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout
        )

    def wait_until_page_does_not_contain_leave_configure_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_configure_leave_period(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_CONFIGURE_LEAVE_PERIOD, timeout)

    def wait_until_page_does_not_contain_leave_configure_leave_types(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_CONFIGURE_LEAVE_TYPES, timeout)

    def wait_until_page_does_not_contain_leave_configure_work_week(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_CONFIGURE_WORK_WEEK, timeout)

    def wait_until_page_does_not_contain_leave_configure_holidays(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_CONFIGURE_HOLIDAYS, timeout)

    def wait_until_page_does_not_contain_leave_leave_list_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_LEAVE_LIST_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_leave_assign_leave_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_timesheets_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_TIMESHEETS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_timesheets_my_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_TIMESHEETS_MY_TIMESHEETS, timeout)

    def wait_until_page_does_not_contain_time_timesheets_employee_timesheets(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_page_does_not_contain_time_attendance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_ATTENDANCE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_attendance_my_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_ATTENDANCE_MY_RECORDS, timeout)

    def wait_until_page_does_not_contain_time_attendance_punch_in_out(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_ATTENDANCE_PUNCH_IN_OUT, timeout)

    def wait_until_page_does_not_contain_time_attendance_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_does_not_contain_time_attendance_configuration(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_ATTENDANCE_CONFIGURATION, timeout)

    def wait_until_page_does_not_contain_time_reports_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_REPORTS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_reports_project_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_REPORTS_PROJECT_REPORTS, timeout)

    def wait_until_page_does_not_contain_time_reports_employee_reports(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_REPORTS_EMPLOYEE_REPORTS, timeout)

    def wait_until_page_does_not_contain_time_reports_attendance_summary(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_REPORTS_ATTENDANCE_SUMMARY, timeout)

    def wait_until_page_does_not_contain_time_project_info_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_PROJECT_INFO_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_time_project_info_customers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_PROJECT_INFO_CUSTOMERS, timeout)

    def wait_until_page_does_not_contain_time_project_info_projects(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.TIME_PROJECT_INFO_PROJECTS, timeout)

    def wait_until_page_does_not_contain_recruitment_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.RECRUITMENT_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_recruitment_candidates_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.RECRUITMENT_CANDIDATES_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_recruitment_vacancies_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.RECRUITMENT_VACANCIES_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_my_info_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MY_INFO_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_performance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_performance_configure_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_performance_configure_kpis(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_CONFIGURE_KPIS, timeout)

    def wait_until_page_does_not_contain_performance_configure_trackers(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_CONFIGURE_TRACKERS, timeout)

    def wait_until_page_does_not_contain_performance_manage_reviews_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_performance_manage_reviews_manage_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS, timeout)

    def wait_until_page_does_not_contain_performance_manage_reviews_my_reviews(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS, timeout)

    def wait_until_page_does_not_contain_performance_manage_reviews_review_list(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST, timeout)

    def wait_until_page_does_not_contain_performance_my_trackers_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_performance_employee_trackers_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_dashboard_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.DASHBOARD_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_directory_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.DIRECTORY_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_maintenance_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MAINTENANCE_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_maintenance_purge_records_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_maintenance_purge_records_employee_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS, timeout)

    def wait_until_page_does_not_contain_maintenance_purge_records_candidate_records(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS, timeout)

    def wait_until_page_does_not_contain_maintenance_access_records_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU, timeout)

    def wait_until_page_does_not_contain_buzz_main_menu(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_page_does_not_contains_element(self.BUZZ_MAIN_MENU, timeout)

    def wait_until_admin_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_MAIN_MENU, timeout)

    def wait_until_admin_user_management_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_MAIN_MENU, timeout)

    def wait_until_admin_user_management_users_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_USERS, timeout)

    def wait_until_admin_user_management_optional_fields_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS, timeout)

    def wait_until_admin_user_management_custom_fields_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS, timeout)

    def wait_until_admin_user_management_data_import_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT, timeout)

    def wait_until_admin_user_management_reporting_methods_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS, timeout)

    def wait_until_admin_user_management_termination_reasons_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS, timeout)

    def wait_until_admin_user_management_my_timesheets_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS, timeout)

    def wait_until_admin_user_management_employee_timesheets_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_admin_user_management_kpis_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_KPIS, timeout)

    def wait_until_admin_user_management_trackers_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_TRACKERS, timeout)

    def wait_until_admin_user_management_employee_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS, timeout)

    def wait_until_admin_user_management_candidate_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS, timeout)

    def wait_until_admin_job_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_MAIN_MENU, timeout)

    def wait_until_admin_job_job_titles_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_JOB_TITLES, timeout)

    def wait_until_admin_job_pay_grades_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_PAY_GRADES, timeout)

    def wait_until_admin_job_employment_status_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_EMPLOYMENT_STATUS, timeout)

    def wait_until_admin_job_job_categories_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_JOB_CATEGORIES, timeout)

    def wait_until_admin_job_work_shifts_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_WORK_SHIFTS, timeout)

    def wait_until_admin_job_my_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_MY_RECORDS, timeout)

    def wait_until_admin_job_punch_in_out_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_PUNCH_IN_OUT, timeout)

    def wait_until_admin_job_employee_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_EMPLOYEE_RECORDS, timeout)

    def wait_until_admin_job_configuration_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_CONFIGURATION, timeout)

    def wait_until_admin_job_manage_reviews_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_MANAGE_REVIEWS, timeout)

    def wait_until_admin_job_my_reviews_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_MY_REVIEWS, timeout)

    def wait_until_admin_job_review_list_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_JOB_REVIEW_LIST, timeout)

    def wait_until_admin_organization_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_MAIN_MENU, timeout)

    def wait_until_admin_organization_general_information_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION, timeout)

    def wait_until_admin_organization_locations_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_LOCATIONS, timeout)

    def wait_until_admin_organization_structure_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_STRUCTURE, timeout)

    def wait_until_admin_organization_add_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_employee_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_my_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_project_reports_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_PROJECT_REPORTS, timeout)

    def wait_until_admin_organization_employee_reports_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS, timeout)

    def wait_until_admin_organization_attendance_summary_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY, timeout)

    def wait_until_admin_qualifications_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_MAIN_MENU, timeout)

    def wait_until_admin_qualifications_skills_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_SKILLS, timeout)

    def wait_until_admin_qualifications_education_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_EDUCATION, timeout)

    def wait_until_admin_qualifications_licenses_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_LICENSES, timeout)

    def wait_until_admin_qualifications_languages_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_LANGUAGES, timeout)

    def wait_until_admin_qualifications_memberships_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS, timeout)

    def wait_until_admin_qualifications_leave_entitlements_and_usage_report_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_admin_qualifications_my_leave_entitlements_and_usage_report_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_admin_qualifications_customers_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_CUSTOMERS, timeout)

    def wait_until_admin_qualifications_projects_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_QUALIFICATIONS_PROJECTS, timeout)

    def wait_until_admin_nationalities_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_NATIONALITIES_MAIN_MENU, timeout)

    def wait_until_admin_nationalities_leave_period_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_NATIONALITIES_LEAVE_PERIOD, timeout)

    def wait_until_admin_nationalities_leave_types_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_NATIONALITIES_LEAVE_TYPES, timeout)

    def wait_until_admin_nationalities_work_week_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_NATIONALITIES_WORK_WEEK, timeout)

    def wait_until_admin_nationalities_holidays_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_NATIONALITIES_HOLIDAYS, timeout)

    def wait_until_admin_corporate_branding_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU, timeout)

    def wait_until_admin_configuration_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_admin_configuration_email_configuration_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION, timeout)

    def wait_until_admin_configuration_email_subscriptions_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS, timeout)

    def wait_until_admin_configuration_localization_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_LOCALIZATION, timeout)

    def wait_until_admin_configuration_language_packages_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES, timeout)

    def wait_until_admin_configuration_modules_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_MODULES, timeout)

    def wait_until_admin_configuration_social_media_authentication_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION, timeout)

    def wait_until_admin_configuration_register_oauth_client_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT, timeout)

    def wait_until_pim_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_MAIN_MENU, timeout)

    def wait_until_pim_configuration_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_pim_configuration_optional_fields_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_OPTIONAL_FIELDS, timeout)

    def wait_until_pim_configuration_custom_fields_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_CUSTOM_FIELDS, timeout)

    def wait_until_pim_configuration_data_import_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_DATA_IMPORT, timeout)

    def wait_until_pim_configuration_reporting_methods_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_REPORTING_METHODS, timeout)

    def wait_until_pim_configuration_termination_reasons_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_CONFIGURATION_TERMINATION_REASONS, timeout)

    def wait_until_pim_employee_list_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_EMPLOYEE_LIST_MAIN_MENU, timeout)

    def wait_until_pim_add_employee_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_ADD_EMPLOYEE_MAIN_MENU, timeout)

    def wait_until_pim_reports_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PIM_REPORTS_MAIN_MENU, timeout)

    def wait_until_leave_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_MAIN_MENU, timeout)

    def wait_until_leave_apply_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_APPLY_MAIN_MENU, timeout)

    def wait_until_leave_my_leave_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_MY_LEAVE_MAIN_MENU, timeout)

    def wait_until_leave_entitlements_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_ENTITLEMENTS_MAIN_MENU, timeout)

    def wait_until_leave_entitlements_add_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS, timeout)

    def wait_until_leave_entitlements_employee_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_leave_entitlements_my_entitlements_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS, timeout)

    def wait_until_leave_reports_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_REPORTS_MAIN_MENU, timeout)

    def wait_until_leave_reports_leave_entitlements_and_usage_report_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_leave_reports_my_leave_entitlements_and_usage_report_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_leave_configure_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_leave_configure_leave_period_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_CONFIGURE_LEAVE_PERIOD, timeout)

    def wait_until_leave_configure_leave_types_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_CONFIGURE_LEAVE_TYPES, timeout)

    def wait_until_leave_configure_work_week_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_CONFIGURE_WORK_WEEK, timeout)

    def wait_until_leave_configure_holidays_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_CONFIGURE_HOLIDAYS, timeout)

    def wait_until_leave_leave_list_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_LEAVE_LIST_MAIN_MENU, timeout)

    def wait_until_leave_assign_leave_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU, timeout)

    def wait_until_time_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_MAIN_MENU, timeout)

    def wait_until_time_timesheets_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_TIMESHEETS_MAIN_MENU, timeout)

    def wait_until_time_timesheets_my_timesheets_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_TIMESHEETS_MY_TIMESHEETS, timeout)

    def wait_until_time_timesheets_employee_timesheets_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_time_attendance_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_ATTENDANCE_MAIN_MENU, timeout)

    def wait_until_time_attendance_my_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_ATTENDANCE_MY_RECORDS, timeout)

    def wait_until_time_attendance_punch_in_out_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_ATTENDANCE_PUNCH_IN_OUT, timeout)

    def wait_until_time_attendance_employee_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS, timeout)

    def wait_until_time_attendance_configuration_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_ATTENDANCE_CONFIGURATION, timeout)

    def wait_until_time_reports_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_REPORTS_MAIN_MENU, timeout)

    def wait_until_time_reports_project_reports_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_REPORTS_PROJECT_REPORTS, timeout)

    def wait_until_time_reports_employee_reports_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_REPORTS_EMPLOYEE_REPORTS, timeout)

    def wait_until_time_reports_attendance_summary_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_REPORTS_ATTENDANCE_SUMMARY, timeout)

    def wait_until_time_project_info_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_PROJECT_INFO_MAIN_MENU, timeout)

    def wait_until_time_project_info_customers_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_PROJECT_INFO_CUSTOMERS, timeout)

    def wait_until_time_project_info_projects_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.TIME_PROJECT_INFO_PROJECTS, timeout)

    def wait_until_recruitment_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.RECRUITMENT_MAIN_MENU, timeout)

    def wait_until_recruitment_candidates_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.RECRUITMENT_CANDIDATES_MAIN_MENU, timeout)

    def wait_until_recruitment_vacancies_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.RECRUITMENT_VACANCIES_MAIN_MENU, timeout)

    def wait_until_my_info_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MY_INFO_MAIN_MENU, timeout)

    def wait_until_performance_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MAIN_MENU, timeout)

    def wait_until_performance_configure_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_performance_configure_kpis_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_CONFIGURE_KPIS, timeout)

    def wait_until_performance_configure_trackers_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_CONFIGURE_TRACKERS, timeout)

    def wait_until_performance_manage_reviews_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU, timeout)

    def wait_until_performance_manage_reviews_manage_reviews_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS, timeout)

    def wait_until_performance_manage_reviews_my_reviews_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS, timeout)

    def wait_until_performance_manage_reviews_review_list_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST, timeout)

    def wait_until_performance_my_trackers_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU, timeout)

    def wait_until_performance_employee_trackers_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU, timeout)

    def wait_until_dashboard_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.DASHBOARD_MAIN_MENU, timeout)

    def wait_until_directory_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.DIRECTORY_MAIN_MENU, timeout)

    def wait_until_maintenance_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MAINTENANCE_MAIN_MENU, timeout)

    def wait_until_maintenance_purge_records_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU, timeout)

    def wait_until_maintenance_purge_records_employee_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS, timeout)

    def wait_until_maintenance_purge_records_candidate_records_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS, timeout)

    def wait_until_maintenance_access_records_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU, timeout)

    def wait_until_buzz_main_menu_is_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_visible(self.BUZZ_MAIN_MENU, timeout)

    def wait_until_admin_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_MAIN_MENU, timeout)

    def wait_until_admin_user_management_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_MAIN_MENU, timeout)

    def wait_until_admin_user_management_users_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_USERS, timeout)

    def wait_until_admin_user_management_optional_fields_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS, timeout)

    def wait_until_admin_user_management_custom_fields_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS, timeout)

    def wait_until_admin_user_management_data_import_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT, timeout)

    def wait_until_admin_user_management_reporting_methods_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS, timeout)

    def wait_until_admin_user_management_termination_reasons_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS, timeout)

    def wait_until_admin_user_management_my_timesheets_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS, timeout)

    def wait_until_admin_user_management_employee_timesheets_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_admin_user_management_kpis_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_KPIS, timeout)

    def wait_until_admin_user_management_trackers_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_TRACKERS, timeout)

    def wait_until_admin_user_management_employee_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS, timeout)

    def wait_until_admin_user_management_candidate_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS, timeout)

    def wait_until_admin_job_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_MAIN_MENU, timeout)

    def wait_until_admin_job_job_titles_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_JOB_TITLES, timeout)

    def wait_until_admin_job_pay_grades_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_PAY_GRADES, timeout)

    def wait_until_admin_job_employment_status_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_EMPLOYMENT_STATUS, timeout)

    def wait_until_admin_job_job_categories_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_JOB_CATEGORIES, timeout)

    def wait_until_admin_job_work_shifts_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_WORK_SHIFTS, timeout)

    def wait_until_admin_job_my_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_MY_RECORDS, timeout)

    def wait_until_admin_job_punch_in_out_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_PUNCH_IN_OUT, timeout)

    def wait_until_admin_job_employee_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_EMPLOYEE_RECORDS, timeout)

    def wait_until_admin_job_configuration_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_CONFIGURATION, timeout)

    def wait_until_admin_job_manage_reviews_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_MANAGE_REVIEWS, timeout)

    def wait_until_admin_job_my_reviews_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_MY_REVIEWS, timeout)

    def wait_until_admin_job_review_list_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_JOB_REVIEW_LIST, timeout)

    def wait_until_admin_organization_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_MAIN_MENU, timeout)

    def wait_until_admin_organization_general_information_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION, timeout)

    def wait_until_admin_organization_locations_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_LOCATIONS, timeout)

    def wait_until_admin_organization_structure_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_STRUCTURE, timeout)

    def wait_until_admin_organization_add_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_employee_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_my_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS, timeout)

    def wait_until_admin_organization_project_reports_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_PROJECT_REPORTS, timeout)

    def wait_until_admin_organization_employee_reports_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS, timeout)

    def wait_until_admin_organization_attendance_summary_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY, timeout)

    def wait_until_admin_qualifications_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_MAIN_MENU, timeout)

    def wait_until_admin_qualifications_skills_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_SKILLS, timeout)

    def wait_until_admin_qualifications_education_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_EDUCATION, timeout)

    def wait_until_admin_qualifications_licenses_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_LICENSES, timeout)

    def wait_until_admin_qualifications_languages_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_LANGUAGES, timeout)

    def wait_until_admin_qualifications_memberships_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS, timeout)

    def wait_until_admin_qualifications_leave_entitlements_and_usage_report_is_not_visible(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_admin_qualifications_my_leave_entitlements_and_usage_report_is_not_visible(
        self, timeout=GLOBAL_TIMEOUT
    ):
        self.wait_until_element_is_not_visible(
            self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout
        )

    def wait_until_admin_qualifications_customers_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_CUSTOMERS, timeout)

    def wait_until_admin_qualifications_projects_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_QUALIFICATIONS_PROJECTS, timeout)

    def wait_until_admin_nationalities_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_NATIONALITIES_MAIN_MENU, timeout)

    def wait_until_admin_nationalities_leave_period_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_NATIONALITIES_LEAVE_PERIOD, timeout)

    def wait_until_admin_nationalities_leave_types_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_NATIONALITIES_LEAVE_TYPES, timeout)

    def wait_until_admin_nationalities_work_week_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_NATIONALITIES_WORK_WEEK, timeout)

    def wait_until_admin_nationalities_holidays_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_NATIONALITIES_HOLIDAYS, timeout)

    def wait_until_admin_corporate_branding_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU, timeout)

    def wait_until_admin_configuration_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_admin_configuration_email_configuration_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION, timeout)

    def wait_until_admin_configuration_email_subscriptions_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS, timeout)

    def wait_until_admin_configuration_localization_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_LOCALIZATION, timeout)

    def wait_until_admin_configuration_language_packages_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES, timeout)

    def wait_until_admin_configuration_modules_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_MODULES, timeout)

    def wait_until_admin_configuration_social_media_authentication_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION, timeout)

    def wait_until_admin_configuration_register_oauth_client_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT, timeout)

    def wait_until_pim_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_MAIN_MENU, timeout)

    def wait_until_pim_configuration_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_MAIN_MENU, timeout)

    def wait_until_pim_configuration_optional_fields_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_OPTIONAL_FIELDS, timeout)

    def wait_until_pim_configuration_custom_fields_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_CUSTOM_FIELDS, timeout)

    def wait_until_pim_configuration_data_import_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_DATA_IMPORT, timeout)

    def wait_until_pim_configuration_reporting_methods_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_REPORTING_METHODS, timeout)

    def wait_until_pim_configuration_termination_reasons_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_CONFIGURATION_TERMINATION_REASONS, timeout)

    def wait_until_pim_employee_list_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_EMPLOYEE_LIST_MAIN_MENU, timeout)

    def wait_until_pim_add_employee_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_ADD_EMPLOYEE_MAIN_MENU, timeout)

    def wait_until_pim_reports_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PIM_REPORTS_MAIN_MENU, timeout)

    def wait_until_leave_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_MAIN_MENU, timeout)

    def wait_until_leave_apply_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_APPLY_MAIN_MENU, timeout)

    def wait_until_leave_my_leave_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_MY_LEAVE_MAIN_MENU, timeout)

    def wait_until_leave_entitlements_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_ENTITLEMENTS_MAIN_MENU, timeout)

    def wait_until_leave_entitlements_add_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS, timeout)

    def wait_until_leave_entitlements_employee_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS, timeout)

    def wait_until_leave_entitlements_my_entitlements_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS, timeout)

    def wait_until_leave_reports_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_REPORTS_MAIN_MENU, timeout)

    def wait_until_leave_reports_leave_entitlements_and_usage_report_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_leave_reports_my_leave_entitlements_and_usage_report_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, timeout)

    def wait_until_leave_configure_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_leave_configure_leave_period_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_CONFIGURE_LEAVE_PERIOD, timeout)

    def wait_until_leave_configure_leave_types_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_CONFIGURE_LEAVE_TYPES, timeout)

    def wait_until_leave_configure_work_week_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_CONFIGURE_WORK_WEEK, timeout)

    def wait_until_leave_configure_holidays_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_CONFIGURE_HOLIDAYS, timeout)

    def wait_until_leave_leave_list_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_LEAVE_LIST_MAIN_MENU, timeout)

    def wait_until_leave_assign_leave_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU, timeout)

    def wait_until_time_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_MAIN_MENU, timeout)

    def wait_until_time_timesheets_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_TIMESHEETS_MAIN_MENU, timeout)

    def wait_until_time_timesheets_my_timesheets_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_TIMESHEETS_MY_TIMESHEETS, timeout)

    def wait_until_time_timesheets_employee_timesheets_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS, timeout)

    def wait_until_time_attendance_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_ATTENDANCE_MAIN_MENU, timeout)

    def wait_until_time_attendance_my_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_ATTENDANCE_MY_RECORDS, timeout)

    def wait_until_time_attendance_punch_in_out_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_ATTENDANCE_PUNCH_IN_OUT, timeout)

    def wait_until_time_attendance_employee_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS, timeout)

    def wait_until_time_attendance_configuration_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_ATTENDANCE_CONFIGURATION, timeout)

    def wait_until_time_reports_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_REPORTS_MAIN_MENU, timeout)

    def wait_until_time_reports_project_reports_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_REPORTS_PROJECT_REPORTS, timeout)

    def wait_until_time_reports_employee_reports_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_REPORTS_EMPLOYEE_REPORTS, timeout)

    def wait_until_time_reports_attendance_summary_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_REPORTS_ATTENDANCE_SUMMARY, timeout)

    def wait_until_time_project_info_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_PROJECT_INFO_MAIN_MENU, timeout)

    def wait_until_time_project_info_customers_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_PROJECT_INFO_CUSTOMERS, timeout)

    def wait_until_time_project_info_projects_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.TIME_PROJECT_INFO_PROJECTS, timeout)

    def wait_until_recruitment_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.RECRUITMENT_MAIN_MENU, timeout)

    def wait_until_recruitment_candidates_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.RECRUITMENT_CANDIDATES_MAIN_MENU, timeout)

    def wait_until_recruitment_vacancies_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.RECRUITMENT_VACANCIES_MAIN_MENU, timeout)

    def wait_until_my_info_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MY_INFO_MAIN_MENU, timeout)

    def wait_until_performance_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MAIN_MENU, timeout)

    def wait_until_performance_configure_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_CONFIGURE_MAIN_MENU, timeout)

    def wait_until_performance_configure_kpis_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_CONFIGURE_KPIS, timeout)

    def wait_until_performance_configure_trackers_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_CONFIGURE_TRACKERS, timeout)

    def wait_until_performance_manage_reviews_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU, timeout)

    def wait_until_performance_manage_reviews_manage_reviews_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS, timeout)

    def wait_until_performance_manage_reviews_my_reviews_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS, timeout)

    def wait_until_performance_manage_reviews_review_list_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST, timeout)

    def wait_until_performance_my_trackers_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU, timeout)

    def wait_until_performance_employee_trackers_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU, timeout)

    def wait_until_dashboard_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.DASHBOARD_MAIN_MENU, timeout)

    def wait_until_directory_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.DIRECTORY_MAIN_MENU, timeout)

    def wait_until_maintenance_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MAINTENANCE_MAIN_MENU, timeout)

    def wait_until_maintenance_purge_records_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU, timeout)

    def wait_until_maintenance_purge_records_employee_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS, timeout)

    def wait_until_maintenance_purge_records_candidate_records_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS, timeout)

    def wait_until_maintenance_access_records_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU, timeout)

    def wait_until_buzz_main_menu_is_not_visible(self, timeout=GLOBAL_TIMEOUT):
        self.wait_until_element_is_not_visible(self.BUZZ_MAIN_MENU, timeout)

    def click_on_admin_main_menu(self):
        self.click_element(self.ADMIN_MAIN_MENU)

    def click_on_admin_user_management_main_menu(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_MAIN_MENU)

    def click_on_admin_user_management_users(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_USERS)

    def click_on_admin_user_management_optional_fields(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS)

    def click_on_admin_user_management_custom_fields(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS)

    def click_on_admin_user_management_data_import(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT)

    def click_on_admin_user_management_reporting_methods(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS)

    def click_on_admin_user_management_termination_reasons(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS)

    def click_on_admin_user_management_my_timesheets(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS)

    def click_on_admin_user_management_employee_timesheets(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS)

    def click_on_admin_user_management_kpis(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_KPIS)

    def click_on_admin_user_management_trackers(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_TRACKERS)

    def click_on_admin_user_management_employee_records(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS)

    def click_on_admin_user_management_candidate_records(self):
        self.click_element(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS)

    def click_on_admin_job_main_menu(self):
        self.click_element(self.ADMIN_JOB_MAIN_MENU)

    def click_on_admin_job_job_titles(self):
        self.click_element(self.ADMIN_JOB_JOB_TITLES)

    def click_on_admin_job_pay_grades(self):
        self.click_element(self.ADMIN_JOB_PAY_GRADES)

    def click_on_admin_job_employment_status(self):
        self.click_element(self.ADMIN_JOB_EMPLOYMENT_STATUS)

    def click_on_admin_job_job_categories(self):
        self.click_element(self.ADMIN_JOB_JOB_CATEGORIES)

    def click_on_admin_job_work_shifts(self):
        self.click_element(self.ADMIN_JOB_WORK_SHIFTS)

    def click_on_admin_job_my_records(self):
        self.click_element(self.ADMIN_JOB_MY_RECORDS)

    def click_on_admin_job_punch_in_out(self):
        self.click_element(self.ADMIN_JOB_PUNCH_IN_OUT)

    def click_on_admin_job_employee_records(self):
        self.click_element(self.ADMIN_JOB_EMPLOYEE_RECORDS)

    def click_on_admin_job_configuration(self):
        self.click_element(self.ADMIN_JOB_CONFIGURATION)

    def click_on_admin_job_manage_reviews(self):
        self.click_element(self.ADMIN_JOB_MANAGE_REVIEWS)

    def click_on_admin_job_my_reviews(self):
        self.click_element(self.ADMIN_JOB_MY_REVIEWS)

    def click_on_admin_job_review_list(self):
        self.click_element(self.ADMIN_JOB_REVIEW_LIST)

    def click_on_admin_organization_main_menu(self):
        self.click_element(self.ADMIN_ORGANIZATION_MAIN_MENU)

    def click_on_admin_organization_general_information(self):
        self.click_element(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION)

    def click_on_admin_organization_locations(self):
        self.click_element(self.ADMIN_ORGANIZATION_LOCATIONS)

    def click_on_admin_organization_structure(self):
        self.click_element(self.ADMIN_ORGANIZATION_STRUCTURE)

    def click_on_admin_organization_add_entitlements(self):
        self.click_element(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS)

    def click_on_admin_organization_employee_entitlements(self):
        self.click_element(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS)

    def click_on_admin_organization_my_entitlements(self):
        self.click_element(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS)

    def click_on_admin_organization_project_reports(self):
        self.click_element(self.ADMIN_ORGANIZATION_PROJECT_REPORTS)

    def click_on_admin_organization_employee_reports(self):
        self.click_element(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS)

    def click_on_admin_organization_attendance_summary(self):
        self.click_element(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY)

    def click_on_admin_qualifications_main_menu(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_MAIN_MENU)

    def click_on_admin_qualifications_skills(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_SKILLS)

    def click_on_admin_qualifications_education(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_EDUCATION)

    def click_on_admin_qualifications_licenses(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_LICENSES)

    def click_on_admin_qualifications_languages(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_LANGUAGES)

    def click_on_admin_qualifications_memberships(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS)

    def click_on_admin_qualifications_leave_entitlements_and_usage_report(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def click_on_admin_qualifications_my_leave_entitlements_and_usage_report(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def click_on_admin_qualifications_customers(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_CUSTOMERS)

    def click_on_admin_qualifications_projects(self):
        self.click_element(self.ADMIN_QUALIFICATIONS_PROJECTS)

    def click_on_admin_nationalities_main_menu(self):
        self.click_element(self.ADMIN_NATIONALITIES_MAIN_MENU)

    def click_on_admin_nationalities_leave_period(self):
        self.click_element(self.ADMIN_NATIONALITIES_LEAVE_PERIOD)

    def click_on_admin_nationalities_leave_types(self):
        self.click_element(self.ADMIN_NATIONALITIES_LEAVE_TYPES)

    def click_on_admin_nationalities_work_week(self):
        self.click_element(self.ADMIN_NATIONALITIES_WORK_WEEK)

    def click_on_admin_nationalities_holidays(self):
        self.click_element(self.ADMIN_NATIONALITIES_HOLIDAYS)

    def click_on_admin_corporate_branding_main_menu(self):
        self.click_element(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU)

    def click_on_admin_configuration_main_menu(self):
        self.click_element(self.ADMIN_CONFIGURATION_MAIN_MENU)

    def click_on_admin_configuration_email_configuration(self):
        self.click_element(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION)

    def click_on_admin_configuration_email_subscriptions(self):
        self.click_element(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS)

    def click_on_admin_configuration_localization(self):
        self.click_element(self.ADMIN_CONFIGURATION_LOCALIZATION)

    def click_on_admin_configuration_language_packages(self):
        self.click_element(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES)

    def click_on_admin_configuration_modules(self):
        self.click_element(self.ADMIN_CONFIGURATION_MODULES)

    def click_on_admin_configuration_social_media_authentication(self):
        self.click_element(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION)

    def click_on_admin_configuration_register_oauth_client(self):
        self.click_element(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT)

    def click_on_pim_main_menu(self):
        self.click_element(self.PIM_MAIN_MENU)

    def click_on_pim_configuration_main_menu(self):
        self.click_element(self.PIM_CONFIGURATION_MAIN_MENU)

    def click_on_pim_configuration_optional_fields(self):
        self.click_element(self.PIM_CONFIGURATION_OPTIONAL_FIELDS)

    def click_on_pim_configuration_custom_fields(self):
        self.click_element(self.PIM_CONFIGURATION_CUSTOM_FIELDS)

    def click_on_pim_configuration_data_import(self):
        self.click_element(self.PIM_CONFIGURATION_DATA_IMPORT)

    def click_on_pim_configuration_reporting_methods(self):
        self.click_element(self.PIM_CONFIGURATION_REPORTING_METHODS)

    def click_on_pim_configuration_termination_reasons(self):
        self.click_element(self.PIM_CONFIGURATION_TERMINATION_REASONS)

    def click_on_pim_employee_list_main_menu(self):
        self.click_element(self.PIM_EMPLOYEE_LIST_MAIN_MENU)

    def click_on_pim_add_employee_main_menu(self):
        self.click_element(self.PIM_ADD_EMPLOYEE_MAIN_MENU)

    def click_on_pim_reports_main_menu(self):
        self.click_element(self.PIM_REPORTS_MAIN_MENU)

    def click_on_leave_main_menu(self):
        self.click_element(self.LEAVE_MAIN_MENU)

    def click_on_leave_apply_main_menu(self):
        self.click_element(self.LEAVE_APPLY_MAIN_MENU)

    def click_on_leave_my_leave_main_menu(self):
        self.click_element(self.LEAVE_MY_LEAVE_MAIN_MENU)

    def click_on_leave_entitlements_main_menu(self):
        self.click_element(self.LEAVE_ENTITLEMENTS_MAIN_MENU)

    def click_on_leave_entitlements_add_entitlements(self):
        self.click_element(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS)

    def click_on_leave_entitlements_employee_entitlements(self):
        self.click_element(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS)

    def click_on_leave_entitlements_my_entitlements(self):
        self.click_element(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS)

    def click_on_leave_reports_main_menu(self):
        self.click_element(self.LEAVE_REPORTS_MAIN_MENU)

    def click_on_leave_reports_leave_entitlements_and_usage_report(self):
        self.click_element(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def click_on_leave_reports_my_leave_entitlements_and_usage_report(self):
        self.click_element(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def click_on_leave_configure_main_menu(self):
        self.click_element(self.LEAVE_CONFIGURE_MAIN_MENU)

    def click_on_leave_configure_leave_period(self):
        self.click_element(self.LEAVE_CONFIGURE_LEAVE_PERIOD)

    def click_on_leave_configure_leave_types(self):
        self.click_element(self.LEAVE_CONFIGURE_LEAVE_TYPES)

    def click_on_leave_configure_work_week(self):
        self.click_element(self.LEAVE_CONFIGURE_WORK_WEEK)

    def click_on_leave_configure_holidays(self):
        self.click_element(self.LEAVE_CONFIGURE_HOLIDAYS)

    def click_on_leave_leave_list_main_menu(self):
        self.click_element(self.LEAVE_LEAVE_LIST_MAIN_MENU)

    def click_on_leave_assign_leave_main_menu(self):
        self.click_element(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU)

    def click_on_time_main_menu(self):
        self.click_element(self.TIME_MAIN_MENU)

    def click_on_time_timesheets_main_menu(self):
        self.click_element(self.TIME_TIMESHEETS_MAIN_MENU)

    def click_on_time_timesheets_my_timesheets(self):
        self.click_element(self.TIME_TIMESHEETS_MY_TIMESHEETS)

    def click_on_time_timesheets_employee_timesheets(self):
        self.click_element(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS)

    def click_on_time_attendance_main_menu(self):
        self.click_element(self.TIME_ATTENDANCE_MAIN_MENU)

    def click_on_time_attendance_my_records(self):
        self.click_element(self.TIME_ATTENDANCE_MY_RECORDS)

    def click_on_time_attendance_punch_in_out(self):
        self.click_element(self.TIME_ATTENDANCE_PUNCH_IN_OUT)

    def click_on_time_attendance_employee_records(self):
        self.click_element(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS)

    def click_on_time_attendance_configuration(self):
        self.click_element(self.TIME_ATTENDANCE_CONFIGURATION)

    def click_on_time_reports_main_menu(self):
        self.click_element(self.TIME_REPORTS_MAIN_MENU)

    def click_on_time_reports_project_reports(self):
        self.click_element(self.TIME_REPORTS_PROJECT_REPORTS)

    def click_on_time_reports_employee_reports(self):
        self.click_element(self.TIME_REPORTS_EMPLOYEE_REPORTS)

    def click_on_time_reports_attendance_summary(self):
        self.click_element(self.TIME_REPORTS_ATTENDANCE_SUMMARY)

    def click_on_time_project_info_main_menu(self):
        self.click_element(self.TIME_PROJECT_INFO_MAIN_MENU)

    def click_on_time_project_info_customers(self):
        self.click_element(self.TIME_PROJECT_INFO_CUSTOMERS)

    def click_on_time_project_info_projects(self):
        self.click_element(self.TIME_PROJECT_INFO_PROJECTS)

    def click_on_recruitment_main_menu(self):
        self.click_element(self.RECRUITMENT_MAIN_MENU)

    def click_on_recruitment_candidates_main_menu(self):
        self.click_element(self.RECRUITMENT_CANDIDATES_MAIN_MENU)

    def click_on_recruitment_vacancies_main_menu(self):
        self.click_element(self.RECRUITMENT_VACANCIES_MAIN_MENU)

    def click_on_my_info_main_menu(self):
        self.click_element(self.MY_INFO_MAIN_MENU)

    def click_on_performance_main_menu(self):
        self.click_element(self.PERFORMANCE_MAIN_MENU)

    def click_on_performance_configure_main_menu(self):
        self.click_element(self.PERFORMANCE_CONFIGURE_MAIN_MENU)

    def click_on_performance_configure_kpis(self):
        self.click_element(self.PERFORMANCE_CONFIGURE_KPIS)

    def click_on_performance_configure_trackers(self):
        self.click_element(self.PERFORMANCE_CONFIGURE_TRACKERS)

    def click_on_performance_manage_reviews_main_menu(self):
        self.click_element(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU)

    def click_on_performance_manage_reviews_manage_reviews(self):
        self.click_element(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS)

    def click_on_performance_manage_reviews_my_reviews(self):
        self.click_element(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS)

    def click_on_performance_manage_reviews_review_list(self):
        self.click_element(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST)

    def click_on_performance_my_trackers_main_menu(self):
        self.click_element(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU)

    def click_on_performance_employee_trackers_main_menu(self):
        self.click_element(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU)

    def click_on_dashboard_main_menu(self):
        self.click_element(self.DASHBOARD_MAIN_MENU)

    def click_on_directory_main_menu(self):
        self.click_element(self.DIRECTORY_MAIN_MENU)

    def click_on_maintenance_main_menu(self):
        self.click_element(self.MAINTENANCE_MAIN_MENU)

    def click_on_maintenance_purge_records_main_menu(self):
        self.click_element(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU)

    def click_on_maintenance_purge_records_employee_records(self):
        self.click_element(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS)

    def click_on_maintenance_purge_records_candidate_records(self):
        self.click_element(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS)

    def click_on_maintenance_access_records_main_menu(self):
        self.click_element(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU)

    def click_on_buzz_main_menu(self):
        self.click_element(self.BUZZ_MAIN_MENU)

    def hover_on_admin_main_menu(self):
        self.hover_element(self.ADMIN_MAIN_MENU)

    def hover_on_admin_user_management_main_menu(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_MAIN_MENU)

    def hover_on_admin_user_management_users(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_USERS)

    def hover_on_admin_user_management_optional_fields(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS)

    def hover_on_admin_user_management_custom_fields(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS)

    def hover_on_admin_user_management_data_import(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT)

    def hover_on_admin_user_management_reporting_methods(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS)

    def hover_on_admin_user_management_termination_reasons(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS)

    def hover_on_admin_user_management_my_timesheets(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS)

    def hover_on_admin_user_management_employee_timesheets(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS)

    def hover_on_admin_user_management_kpis(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_KPIS)

    def hover_on_admin_user_management_trackers(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_TRACKERS)

    def hover_on_admin_user_management_employee_records(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS)

    def hover_on_admin_user_management_candidate_records(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS)

    def hover_on_admin_job_main_menu(self):
        self.hover_element(self.ADMIN_JOB_MAIN_MENU)

    def hover_on_admin_job_job_titles(self):
        self.hover_element(self.ADMIN_JOB_JOB_TITLES)

    def hover_on_admin_job_pay_grades(self):
        self.hover_element(self.ADMIN_JOB_PAY_GRADES)

    def hover_on_admin_job_employment_status(self):
        self.hover_element(self.ADMIN_JOB_EMPLOYMENT_STATUS)

    def hover_on_admin_job_job_categories(self):
        self.hover_element(self.ADMIN_JOB_JOB_CATEGORIES)

    def hover_on_admin_job_work_shifts(self):
        self.hover_element(self.ADMIN_JOB_WORK_SHIFTS)

    def hover_on_admin_job_my_records(self):
        self.hover_element(self.ADMIN_JOB_MY_RECORDS)

    def hover_on_admin_job_punch_in_out(self):
        self.hover_element(self.ADMIN_JOB_PUNCH_IN_OUT)

    def hover_on_admin_job_employee_records(self):
        self.hover_element(self.ADMIN_JOB_EMPLOYEE_RECORDS)

    def hover_on_admin_job_configuration(self):
        self.hover_element(self.ADMIN_JOB_CONFIGURATION)

    def hover_on_admin_job_manage_reviews(self):
        self.hover_element(self.ADMIN_JOB_MANAGE_REVIEWS)

    def hover_on_admin_job_my_reviews(self):
        self.hover_element(self.ADMIN_JOB_MY_REVIEWS)

    def hover_on_admin_job_review_list(self):
        self.hover_element(self.ADMIN_JOB_REVIEW_LIST)

    def hover_on_admin_organization_main_menu(self):
        self.hover_element(self.ADMIN_ORGANIZATION_MAIN_MENU)

    def hover_on_admin_organization_general_information(self):
        self.hover_element(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION)

    def hover_on_admin_organization_locations(self):
        self.hover_element(self.ADMIN_ORGANIZATION_LOCATIONS)

    def hover_on_admin_organization_structure(self):
        self.hover_element(self.ADMIN_ORGANIZATION_STRUCTURE)

    def hover_on_admin_organization_add_entitlements(self):
        self.hover_element(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS)

    def hover_on_admin_organization_employee_entitlements(self):
        self.hover_element(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS)

    def hover_on_admin_organization_my_entitlements(self):
        self.hover_element(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS)

    def hover_on_admin_organization_project_reports(self):
        self.hover_element(self.ADMIN_ORGANIZATION_PROJECT_REPORTS)

    def hover_on_admin_organization_employee_reports(self):
        self.hover_element(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS)

    def hover_on_admin_organization_attendance_summary(self):
        self.hover_element(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY)

    def hover_on_admin_qualifications_main_menu(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MAIN_MENU)

    def hover_on_admin_qualifications_skills(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_SKILLS)

    def hover_on_admin_qualifications_education(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_EDUCATION)

    def hover_on_admin_qualifications_licenses(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LICENSES)

    def hover_on_admin_qualifications_languages(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LANGUAGES)

    def hover_on_admin_qualifications_memberships(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS)

    def hover_on_admin_qualifications_leave_entitlements_and_usage_report(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def hover_on_admin_qualifications_my_leave_entitlements_and_usage_report(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def hover_on_admin_qualifications_customers(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_CUSTOMERS)

    def hover_on_admin_qualifications_projects(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_PROJECTS)

    def hover_on_admin_nationalities_main_menu(self):
        self.hover_element(self.ADMIN_NATIONALITIES_MAIN_MENU)

    def hover_on_admin_nationalities_leave_period(self):
        self.hover_element(self.ADMIN_NATIONALITIES_LEAVE_PERIOD)

    def hover_on_admin_nationalities_leave_types(self):
        self.hover_element(self.ADMIN_NATIONALITIES_LEAVE_TYPES)

    def hover_on_admin_nationalities_work_week(self):
        self.hover_element(self.ADMIN_NATIONALITIES_WORK_WEEK)

    def hover_on_admin_nationalities_holidays(self):
        self.hover_element(self.ADMIN_NATIONALITIES_HOLIDAYS)

    def hover_on_admin_corporate_branding_main_menu(self):
        self.hover_element(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU)

    def hover_on_admin_configuration_main_menu(self):
        self.hover_element(self.ADMIN_CONFIGURATION_MAIN_MENU)

    def hover_on_admin_configuration_email_configuration(self):
        self.hover_element(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION)

    def hover_on_admin_configuration_email_subscriptions(self):
        self.hover_element(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS)

    def hover_on_admin_configuration_localization(self):
        self.hover_element(self.ADMIN_CONFIGURATION_LOCALIZATION)

    def hover_on_admin_configuration_language_packages(self):
        self.hover_element(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES)

    def hover_on_admin_configuration_modules(self):
        self.hover_element(self.ADMIN_CONFIGURATION_MODULES)

    def hover_on_admin_configuration_social_media_authentication(self):
        self.hover_element(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION)

    def hover_on_admin_configuration_register_oauth_client(self):
        self.hover_element(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT)

    def hover_on_pim_main_menu(self):
        self.hover_element(self.PIM_MAIN_MENU)

    def hover_on_pim_configuration_main_menu(self):
        self.hover_element(self.PIM_CONFIGURATION_MAIN_MENU)

    def hover_on_pim_configuration_optional_fields(self):
        self.hover_element(self.PIM_CONFIGURATION_OPTIONAL_FIELDS)

    def hover_on_pim_configuration_custom_fields(self):
        self.hover_element(self.PIM_CONFIGURATION_CUSTOM_FIELDS)

    def hover_on_pim_configuration_data_import(self):
        self.hover_element(self.PIM_CONFIGURATION_DATA_IMPORT)

    def hover_on_pim_configuration_reporting_methods(self):
        self.hover_element(self.PIM_CONFIGURATION_REPORTING_METHODS)

    def hover_on_pim_configuration_termination_reasons(self):
        self.hover_element(self.PIM_CONFIGURATION_TERMINATION_REASONS)

    def hover_on_pim_employee_list_main_menu(self):
        self.hover_element(self.PIM_EMPLOYEE_LIST_MAIN_MENU)

    def hover_on_pim_add_employee_main_menu(self):
        self.hover_element(self.PIM_ADD_EMPLOYEE_MAIN_MENU)

    def hover_on_pim_reports_main_menu(self):
        self.hover_element(self.PIM_REPORTS_MAIN_MENU)

    def hover_on_leave_main_menu(self):
        self.hover_element(self.LEAVE_MAIN_MENU)

    def hover_on_leave_apply_main_menu(self):
        self.hover_element(self.LEAVE_APPLY_MAIN_MENU)

    def hover_on_leave_my_leave_main_menu(self):
        self.hover_element(self.LEAVE_MY_LEAVE_MAIN_MENU)

    def hover_on_leave_entitlements_main_menu(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_MAIN_MENU)

    def hover_on_leave_entitlements_add_entitlements(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS)

    def hover_on_leave_entitlements_employee_entitlements(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS)

    def hover_on_leave_entitlements_my_entitlements(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS)

    def hover_on_leave_reports_main_menu(self):
        self.hover_element(self.LEAVE_REPORTS_MAIN_MENU)

    def hover_on_leave_reports_leave_entitlements_and_usage_report(self):
        self.hover_element(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def hover_on_leave_reports_my_leave_entitlements_and_usage_report(self):
        self.hover_element(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def hover_on_leave_configure_main_menu(self):
        self.hover_element(self.LEAVE_CONFIGURE_MAIN_MENU)

    def hover_on_leave_configure_leave_period(self):
        self.hover_element(self.LEAVE_CONFIGURE_LEAVE_PERIOD)

    def hover_on_leave_configure_leave_types(self):
        self.hover_element(self.LEAVE_CONFIGURE_LEAVE_TYPES)

    def hover_on_leave_configure_work_week(self):
        self.hover_element(self.LEAVE_CONFIGURE_WORK_WEEK)

    def hover_on_leave_configure_holidays(self):
        self.hover_element(self.LEAVE_CONFIGURE_HOLIDAYS)

    def hover_on_leave_leave_list_main_menu(self):
        self.hover_element(self.LEAVE_LEAVE_LIST_MAIN_MENU)

    def hover_on_leave_assign_leave_main_menu(self):
        self.hover_element(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU)

    def hover_on_time_main_menu(self):
        self.hover_element(self.TIME_MAIN_MENU)

    def hover_on_time_timesheets_main_menu(self):
        self.hover_element(self.TIME_TIMESHEETS_MAIN_MENU)

    def hover_on_time_timesheets_my_timesheets(self):
        self.hover_element(self.TIME_TIMESHEETS_MY_TIMESHEETS)

    def hover_on_time_timesheets_employee_timesheets(self):
        self.hover_element(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS)

    def hover_on_time_attendance_main_menu(self):
        self.hover_element(self.TIME_ATTENDANCE_MAIN_MENU)

    def hover_on_time_attendance_my_records(self):
        self.hover_element(self.TIME_ATTENDANCE_MY_RECORDS)

    def hover_on_time_attendance_punch_in_out(self):
        self.hover_element(self.TIME_ATTENDANCE_PUNCH_IN_OUT)

    def hover_on_time_attendance_employee_records(self):
        self.hover_element(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS)

    def hover_on_time_attendance_configuration(self):
        self.hover_element(self.TIME_ATTENDANCE_CONFIGURATION)

    def hover_on_time_reports_main_menu(self):
        self.hover_element(self.TIME_REPORTS_MAIN_MENU)

    def hover_on_time_reports_project_reports(self):
        self.hover_element(self.TIME_REPORTS_PROJECT_REPORTS)

    def hover_on_time_reports_employee_reports(self):
        self.hover_element(self.TIME_REPORTS_EMPLOYEE_REPORTS)

    def hover_on_time_reports_attendance_summary(self):
        self.hover_element(self.TIME_REPORTS_ATTENDANCE_SUMMARY)

    def hover_on_time_project_info_main_menu(self):
        self.hover_element(self.TIME_PROJECT_INFO_MAIN_MENU)

    def hover_on_time_project_info_customers(self):
        self.hover_element(self.TIME_PROJECT_INFO_CUSTOMERS)

    def hover_on_time_project_info_projects(self):
        self.hover_element(self.TIME_PROJECT_INFO_PROJECTS)

    def hover_on_recruitment_main_menu(self):
        self.hover_element(self.RECRUITMENT_MAIN_MENU)

    def hover_on_recruitment_candidates_main_menu(self):
        self.hover_element(self.RECRUITMENT_CANDIDATES_MAIN_MENU)

    def hover_on_recruitment_vacancies_main_menu(self):
        self.hover_element(self.RECRUITMENT_VACANCIES_MAIN_MENU)

    def hover_on_my_info_main_menu(self):
        self.hover_element(self.MY_INFO_MAIN_MENU)

    def hover_on_performance_main_menu(self):
        self.hover_element(self.PERFORMANCE_MAIN_MENU)

    def hover_on_performance_configure_main_menu(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_MAIN_MENU)

    def hover_on_performance_configure_kpis(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_KPIS)

    def hover_on_performance_configure_trackers(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_TRACKERS)

    def hover_on_performance_manage_reviews_main_menu(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU)

    def hover_on_performance_manage_reviews_manage_reviews(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS)

    def hover_on_performance_manage_reviews_my_reviews(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS)

    def hover_on_performance_manage_reviews_review_list(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST)

    def hover_on_performance_my_trackers_main_menu(self):
        self.hover_element(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU)

    def hover_on_performance_employee_trackers_main_menu(self):
        self.hover_element(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU)

    def hover_on_dashboard_main_menu(self):
        self.hover_element(self.DASHBOARD_MAIN_MENU)

    def hover_on_directory_main_menu(self):
        self.hover_element(self.DIRECTORY_MAIN_MENU)

    def hover_on_maintenance_main_menu(self):
        self.hover_element(self.MAINTENANCE_MAIN_MENU)

    def hover_on_maintenance_purge_records_main_menu(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU)

    def hover_on_maintenance_purge_records_employee_records(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS)

    def hover_on_maintenance_purge_records_candidate_records(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS)

    def hover_on_maintenance_access_records_main_menu(self):
        self.hover_element(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU)

    def hover_on_buzz_main_menu(self):
        self.hover_element(self.BUZZ_MAIN_MENU)

    def scroll_admin_main_menu_into_view(self):
        self.hover_element(self.ADMIN_MAIN_MENU)

    def scroll_admin_user_management_main_menu_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_MAIN_MENU)

    def scroll_admin_user_management_users_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_USERS)

    def scroll_admin_user_management_optional_fields_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS)

    def scroll_admin_user_management_custom_fields_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS)

    def scroll_admin_user_management_data_import_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT)

    def scroll_admin_user_management_reporting_methods_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS)

    def scroll_admin_user_management_termination_reasons_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS)

    def scroll_admin_user_management_my_timesheets_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS)

    def scroll_admin_user_management_employee_timesheets_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS)

    def scroll_admin_user_management_kpis_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_KPIS)

    def scroll_admin_user_management_trackers_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_TRACKERS)

    def scroll_admin_user_management_employee_records_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS)

    def scroll_admin_user_management_candidate_records_into_view(self):
        self.hover_element(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS)

    def scroll_admin_job_main_menu_into_view(self):
        self.hover_element(self.ADMIN_JOB_MAIN_MENU)

    def scroll_admin_job_job_titles_into_view(self):
        self.hover_element(self.ADMIN_JOB_JOB_TITLES)

    def scroll_admin_job_pay_grades_into_view(self):
        self.hover_element(self.ADMIN_JOB_PAY_GRADES)

    def scroll_admin_job_employment_status_into_view(self):
        self.hover_element(self.ADMIN_JOB_EMPLOYMENT_STATUS)

    def scroll_admin_job_job_categories_into_view(self):
        self.hover_element(self.ADMIN_JOB_JOB_CATEGORIES)

    def scroll_admin_job_work_shifts_into_view(self):
        self.hover_element(self.ADMIN_JOB_WORK_SHIFTS)

    def scroll_admin_job_my_records_into_view(self):
        self.hover_element(self.ADMIN_JOB_MY_RECORDS)

    def scroll_admin_job_punch_in_out_into_view(self):
        self.hover_element(self.ADMIN_JOB_PUNCH_IN_OUT)

    def scroll_admin_job_employee_records_into_view(self):
        self.hover_element(self.ADMIN_JOB_EMPLOYEE_RECORDS)

    def scroll_admin_job_configuration_into_view(self):
        self.hover_element(self.ADMIN_JOB_CONFIGURATION)

    def scroll_admin_job_manage_reviews_into_view(self):
        self.hover_element(self.ADMIN_JOB_MANAGE_REVIEWS)

    def scroll_admin_job_my_reviews_into_view(self):
        self.hover_element(self.ADMIN_JOB_MY_REVIEWS)

    def scroll_admin_job_review_list_into_view(self):
        self.hover_element(self.ADMIN_JOB_REVIEW_LIST)

    def scroll_admin_organization_main_menu_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_MAIN_MENU)

    def scroll_admin_organization_general_information_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION)

    def scroll_admin_organization_locations_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_LOCATIONS)

    def scroll_admin_organization_structure_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_STRUCTURE)

    def scroll_admin_organization_add_entitlements_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS)

    def scroll_admin_organization_employee_entitlements_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS)

    def scroll_admin_organization_my_entitlements_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS)

    def scroll_admin_organization_project_reports_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_PROJECT_REPORTS)

    def scroll_admin_organization_employee_reports_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS)

    def scroll_admin_organization_attendance_summary_into_view(self):
        self.hover_element(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY)

    def scroll_admin_qualifications_main_menu_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MAIN_MENU)

    def scroll_admin_qualifications_skills_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_SKILLS)

    def scroll_admin_qualifications_education_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_EDUCATION)

    def scroll_admin_qualifications_licenses_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LICENSES)

    def scroll_admin_qualifications_languages_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LANGUAGES)

    def scroll_admin_qualifications_memberships_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS)

    def scroll_admin_qualifications_leave_entitlements_and_usage_report_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def scroll_admin_qualifications_my_leave_entitlements_and_usage_report_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def scroll_admin_qualifications_customers_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_CUSTOMERS)

    def scroll_admin_qualifications_projects_into_view(self):
        self.hover_element(self.ADMIN_QUALIFICATIONS_PROJECTS)

    def scroll_admin_nationalities_main_menu_into_view(self):
        self.hover_element(self.ADMIN_NATIONALITIES_MAIN_MENU)

    def scroll_admin_nationalities_leave_period_into_view(self):
        self.hover_element(self.ADMIN_NATIONALITIES_LEAVE_PERIOD)

    def scroll_admin_nationalities_leave_types_into_view(self):
        self.hover_element(self.ADMIN_NATIONALITIES_LEAVE_TYPES)

    def scroll_admin_nationalities_work_week_into_view(self):
        self.hover_element(self.ADMIN_NATIONALITIES_WORK_WEEK)

    def scroll_admin_nationalities_holidays_into_view(self):
        self.hover_element(self.ADMIN_NATIONALITIES_HOLIDAYS)

    def scroll_admin_corporate_branding_main_menu_into_view(self):
        self.hover_element(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU)

    def scroll_admin_configuration_main_menu_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_MAIN_MENU)

    def scroll_admin_configuration_email_configuration_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION)

    def scroll_admin_configuration_email_subscriptions_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS)

    def scroll_admin_configuration_localization_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_LOCALIZATION)

    def scroll_admin_configuration_language_packages_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES)

    def scroll_admin_configuration_modules_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_MODULES)

    def scroll_admin_configuration_social_media_authentication_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION)

    def scroll_admin_configuration_register_oauth_client_into_view(self):
        self.hover_element(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT)

    def scroll_pim_main_menu_into_view(self):
        self.hover_element(self.PIM_MAIN_MENU)

    def scroll_pim_configuration_main_menu_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_MAIN_MENU)

    def scroll_pim_configuration_optional_fields_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_OPTIONAL_FIELDS)

    def scroll_pim_configuration_custom_fields_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_CUSTOM_FIELDS)

    def scroll_pim_configuration_data_import_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_DATA_IMPORT)

    def scroll_pim_configuration_reporting_methods_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_REPORTING_METHODS)

    def scroll_pim_configuration_termination_reasons_into_view(self):
        self.hover_element(self.PIM_CONFIGURATION_TERMINATION_REASONS)

    def scroll_pim_employee_list_main_menu_into_view(self):
        self.hover_element(self.PIM_EMPLOYEE_LIST_MAIN_MENU)

    def scroll_pim_add_employee_main_menu_into_view(self):
        self.hover_element(self.PIM_ADD_EMPLOYEE_MAIN_MENU)

    def scroll_pim_reports_main_menu_into_view(self):
        self.hover_element(self.PIM_REPORTS_MAIN_MENU)

    def scroll_leave_main_menu_into_view(self):
        self.hover_element(self.LEAVE_MAIN_MENU)

    def scroll_leave_apply_main_menu_into_view(self):
        self.hover_element(self.LEAVE_APPLY_MAIN_MENU)

    def scroll_leave_my_leave_main_menu_into_view(self):
        self.hover_element(self.LEAVE_MY_LEAVE_MAIN_MENU)

    def scroll_leave_entitlements_main_menu_into_view(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_MAIN_MENU)

    def scroll_leave_entitlements_add_entitlements_into_view(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS)

    def scroll_leave_entitlements_employee_entitlements_into_view(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS)

    def scroll_leave_entitlements_my_entitlements_into_view(self):
        self.hover_element(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS)

    def scroll_leave_reports_main_menu_into_view(self):
        self.hover_element(self.LEAVE_REPORTS_MAIN_MENU)

    def scroll_leave_reports_leave_entitlements_and_usage_report_into_view(self):
        self.hover_element(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def scroll_leave_reports_my_leave_entitlements_and_usage_report_into_view(self):
        self.hover_element(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def scroll_leave_configure_main_menu_into_view(self):
        self.hover_element(self.LEAVE_CONFIGURE_MAIN_MENU)

    def scroll_leave_configure_leave_period_into_view(self):
        self.hover_element(self.LEAVE_CONFIGURE_LEAVE_PERIOD)

    def scroll_leave_configure_leave_types_into_view(self):
        self.hover_element(self.LEAVE_CONFIGURE_LEAVE_TYPES)

    def scroll_leave_configure_work_week_into_view(self):
        self.hover_element(self.LEAVE_CONFIGURE_WORK_WEEK)

    def scroll_leave_configure_holidays_into_view(self):
        self.hover_element(self.LEAVE_CONFIGURE_HOLIDAYS)

    def scroll_leave_leave_list_main_menu_into_view(self):
        self.hover_element(self.LEAVE_LEAVE_LIST_MAIN_MENU)

    def scroll_leave_assign_leave_main_menu_into_view(self):
        self.hover_element(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU)

    def scroll_time_main_menu_into_view(self):
        self.hover_element(self.TIME_MAIN_MENU)

    def scroll_time_timesheets_main_menu_into_view(self):
        self.hover_element(self.TIME_TIMESHEETS_MAIN_MENU)

    def scroll_time_timesheets_my_timesheets_into_view(self):
        self.hover_element(self.TIME_TIMESHEETS_MY_TIMESHEETS)

    def scroll_time_timesheets_employee_timesheets_into_view(self):
        self.hover_element(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS)

    def scroll_time_attendance_main_menu_into_view(self):
        self.hover_element(self.TIME_ATTENDANCE_MAIN_MENU)

    def scroll_time_attendance_my_records_into_view(self):
        self.hover_element(self.TIME_ATTENDANCE_MY_RECORDS)

    def scroll_time_attendance_punch_in_out_into_view(self):
        self.hover_element(self.TIME_ATTENDANCE_PUNCH_IN_OUT)

    def scroll_time_attendance_employee_records_into_view(self):
        self.hover_element(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS)

    def scroll_time_attendance_configuration_into_view(self):
        self.hover_element(self.TIME_ATTENDANCE_CONFIGURATION)

    def scroll_time_reports_main_menu_into_view(self):
        self.hover_element(self.TIME_REPORTS_MAIN_MENU)

    def scroll_time_reports_project_reports_into_view(self):
        self.hover_element(self.TIME_REPORTS_PROJECT_REPORTS)

    def scroll_time_reports_employee_reports_into_view(self):
        self.hover_element(self.TIME_REPORTS_EMPLOYEE_REPORTS)

    def scroll_time_reports_attendance_summary_into_view(self):
        self.hover_element(self.TIME_REPORTS_ATTENDANCE_SUMMARY)

    def scroll_time_project_info_main_menu_into_view(self):
        self.hover_element(self.TIME_PROJECT_INFO_MAIN_MENU)

    def scroll_time_project_info_customers_into_view(self):
        self.hover_element(self.TIME_PROJECT_INFO_CUSTOMERS)

    def scroll_time_project_info_projects_into_view(self):
        self.hover_element(self.TIME_PROJECT_INFO_PROJECTS)

    def scroll_recruitment_main_menu_into_view(self):
        self.hover_element(self.RECRUITMENT_MAIN_MENU)

    def scroll_recruitment_candidates_main_menu_into_view(self):
        self.hover_element(self.RECRUITMENT_CANDIDATES_MAIN_MENU)

    def scroll_recruitment_vacancies_main_menu_into_view(self):
        self.hover_element(self.RECRUITMENT_VACANCIES_MAIN_MENU)

    def scroll_my_info_main_menu_into_view(self):
        self.hover_element(self.MY_INFO_MAIN_MENU)

    def scroll_performance_main_menu_into_view(self):
        self.hover_element(self.PERFORMANCE_MAIN_MENU)

    def scroll_performance_configure_main_menu_into_view(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_MAIN_MENU)

    def scroll_performance_configure_kpis_into_view(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_KPIS)

    def scroll_performance_configure_trackers_into_view(self):
        self.hover_element(self.PERFORMANCE_CONFIGURE_TRACKERS)

    def scroll_performance_manage_reviews_main_menu_into_view(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU)

    def scroll_performance_manage_reviews_manage_reviews_into_view(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS)

    def scroll_performance_manage_reviews_my_reviews_into_view(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS)

    def scroll_performance_manage_reviews_review_list_into_view(self):
        self.hover_element(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST)

    def scroll_performance_my_trackers_main_menu_into_view(self):
        self.hover_element(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU)

    def scroll_performance_employee_trackers_main_menu_into_view(self):
        self.hover_element(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU)

    def scroll_dashboard_main_menu_into_view(self):
        self.hover_element(self.DASHBOARD_MAIN_MENU)

    def scroll_directory_main_menu_into_view(self):
        self.hover_element(self.DIRECTORY_MAIN_MENU)

    def scroll_maintenance_main_menu_into_view(self):
        self.hover_element(self.MAINTENANCE_MAIN_MENU)

    def scroll_maintenance_purge_records_main_menu_into_view(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU)

    def scroll_maintenance_purge_records_employee_records_into_view(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS)

    def scroll_maintenance_purge_records_candidate_records_into_view(self):
        self.hover_element(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS)

    def scroll_maintenance_access_records_main_menu_into_view(self):
        self.hover_element(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU)

    def scroll_buzz_main_menu_into_view(self):
        self.hover_element(self.BUZZ_MAIN_MENU)

    def enter_text_on_admin_main_menu(self, value):
        self.input_text(self.ADMIN_MAIN_MENU, value)

    def enter_text_on_admin_user_management_main_menu(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_MAIN_MENU, value)

    def enter_text_on_admin_user_management_users(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_USERS, value)

    def enter_text_on_admin_user_management_optional_fields(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS, value)

    def enter_text_on_admin_user_management_custom_fields(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS, value)

    def enter_text_on_admin_user_management_data_import(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT, value)

    def enter_text_on_admin_user_management_reporting_methods(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS, value)

    def enter_text_on_admin_user_management_termination_reasons(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS, value)

    def enter_text_on_admin_user_management_my_timesheets(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS, value)

    def enter_text_on_admin_user_management_employee_timesheets(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS, value)

    def enter_text_on_admin_user_management_kpis(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_KPIS, value)

    def enter_text_on_admin_user_management_trackers(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_TRACKERS, value)

    def enter_text_on_admin_user_management_employee_records(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS, value)

    def enter_text_on_admin_user_management_candidate_records(self, value):
        self.input_text(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS, value)

    def enter_text_on_admin_job_main_menu(self, value):
        self.input_text(self.ADMIN_JOB_MAIN_MENU, value)

    def enter_text_on_admin_job_job_titles(self, value):
        self.input_text(self.ADMIN_JOB_JOB_TITLES, value)

    def enter_text_on_admin_job_pay_grades(self, value):
        self.input_text(self.ADMIN_JOB_PAY_GRADES, value)

    def enter_text_on_admin_job_employment_status(self, value):
        self.input_text(self.ADMIN_JOB_EMPLOYMENT_STATUS, value)

    def enter_text_on_admin_job_job_categories(self, value):
        self.input_text(self.ADMIN_JOB_JOB_CATEGORIES, value)

    def enter_text_on_admin_job_work_shifts(self, value):
        self.input_text(self.ADMIN_JOB_WORK_SHIFTS, value)

    def enter_text_on_admin_job_my_records(self, value):
        self.input_text(self.ADMIN_JOB_MY_RECORDS, value)

    def enter_text_on_admin_job_punch_in_out(self, value):
        self.input_text(self.ADMIN_JOB_PUNCH_IN_OUT, value)

    def enter_text_on_admin_job_employee_records(self, value):
        self.input_text(self.ADMIN_JOB_EMPLOYEE_RECORDS, value)

    def enter_text_on_admin_job_configuration(self, value):
        self.input_text(self.ADMIN_JOB_CONFIGURATION, value)

    def enter_text_on_admin_job_manage_reviews(self, value):
        self.input_text(self.ADMIN_JOB_MANAGE_REVIEWS, value)

    def enter_text_on_admin_job_my_reviews(self, value):
        self.input_text(self.ADMIN_JOB_MY_REVIEWS, value)

    def enter_text_on_admin_job_review_list(self, value):
        self.input_text(self.ADMIN_JOB_REVIEW_LIST, value)

    def enter_text_on_admin_organization_main_menu(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_MAIN_MENU, value)

    def enter_text_on_admin_organization_general_information(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION, value)

    def enter_text_on_admin_organization_locations(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_LOCATIONS, value)

    def enter_text_on_admin_organization_structure(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_STRUCTURE, value)

    def enter_text_on_admin_organization_add_entitlements(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS, value)

    def enter_text_on_admin_organization_employee_entitlements(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS, value)

    def enter_text_on_admin_organization_my_entitlements(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS, value)

    def enter_text_on_admin_organization_project_reports(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_PROJECT_REPORTS, value)

    def enter_text_on_admin_organization_employee_reports(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS, value)

    def enter_text_on_admin_organization_attendance_summary(self, value):
        self.input_text(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY, value)

    def enter_text_on_admin_qualifications_main_menu(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_MAIN_MENU, value)

    def enter_text_on_admin_qualifications_skills(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_SKILLS, value)

    def enter_text_on_admin_qualifications_education(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_EDUCATION, value)

    def enter_text_on_admin_qualifications_licenses(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_LICENSES, value)

    def enter_text_on_admin_qualifications_languages(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_LANGUAGES, value)

    def enter_text_on_admin_qualifications_memberships(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS, value)

    def enter_text_on_admin_qualifications_leave_entitlements_and_usage_report(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, value)

    def enter_text_on_admin_qualifications_my_leave_entitlements_and_usage_report(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, value)

    def enter_text_on_admin_qualifications_customers(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_CUSTOMERS, value)

    def enter_text_on_admin_qualifications_projects(self, value):
        self.input_text(self.ADMIN_QUALIFICATIONS_PROJECTS, value)

    def enter_text_on_admin_nationalities_main_menu(self, value):
        self.input_text(self.ADMIN_NATIONALITIES_MAIN_MENU, value)

    def enter_text_on_admin_nationalities_leave_period(self, value):
        self.input_text(self.ADMIN_NATIONALITIES_LEAVE_PERIOD, value)

    def enter_text_on_admin_nationalities_leave_types(self, value):
        self.input_text(self.ADMIN_NATIONALITIES_LEAVE_TYPES, value)

    def enter_text_on_admin_nationalities_work_week(self, value):
        self.input_text(self.ADMIN_NATIONALITIES_WORK_WEEK, value)

    def enter_text_on_admin_nationalities_holidays(self, value):
        self.input_text(self.ADMIN_NATIONALITIES_HOLIDAYS, value)

    def enter_text_on_admin_corporate_branding_main_menu(self, value):
        self.input_text(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU, value)

    def enter_text_on_admin_configuration_main_menu(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_MAIN_MENU, value)

    def enter_text_on_admin_configuration_email_configuration(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION, value)

    def enter_text_on_admin_configuration_email_subscriptions(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS, value)

    def enter_text_on_admin_configuration_localization(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_LOCALIZATION, value)

    def enter_text_on_admin_configuration_language_packages(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES, value)

    def enter_text_on_admin_configuration_modules(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_MODULES, value)

    def enter_text_on_admin_configuration_social_media_authentication(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION, value)

    def enter_text_on_admin_configuration_register_oauth_client(self, value):
        self.input_text(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT, value)

    def enter_text_on_pim_main_menu(self, value):
        self.input_text(self.PIM_MAIN_MENU, value)

    def enter_text_on_pim_configuration_main_menu(self, value):
        self.input_text(self.PIM_CONFIGURATION_MAIN_MENU, value)

    def enter_text_on_pim_configuration_optional_fields(self, value):
        self.input_text(self.PIM_CONFIGURATION_OPTIONAL_FIELDS, value)

    def enter_text_on_pim_configuration_custom_fields(self, value):
        self.input_text(self.PIM_CONFIGURATION_CUSTOM_FIELDS, value)

    def enter_text_on_pim_configuration_data_import(self, value):
        self.input_text(self.PIM_CONFIGURATION_DATA_IMPORT, value)

    def enter_text_on_pim_configuration_reporting_methods(self, value):
        self.input_text(self.PIM_CONFIGURATION_REPORTING_METHODS, value)

    def enter_text_on_pim_configuration_termination_reasons(self, value):
        self.input_text(self.PIM_CONFIGURATION_TERMINATION_REASONS, value)

    def enter_text_on_pim_employee_list_main_menu(self, value):
        self.input_text(self.PIM_EMPLOYEE_LIST_MAIN_MENU, value)

    def enter_text_on_pim_add_employee_main_menu(self, value):
        self.input_text(self.PIM_ADD_EMPLOYEE_MAIN_MENU, value)

    def enter_text_on_pim_reports_main_menu(self, value):
        self.input_text(self.PIM_REPORTS_MAIN_MENU, value)

    def enter_text_on_leave_main_menu(self, value):
        self.input_text(self.LEAVE_MAIN_MENU, value)

    def enter_text_on_leave_apply_main_menu(self, value):
        self.input_text(self.LEAVE_APPLY_MAIN_MENU, value)

    def enter_text_on_leave_my_leave_main_menu(self, value):
        self.input_text(self.LEAVE_MY_LEAVE_MAIN_MENU, value)

    def enter_text_on_leave_entitlements_main_menu(self, value):
        self.input_text(self.LEAVE_ENTITLEMENTS_MAIN_MENU, value)

    def enter_text_on_leave_entitlements_add_entitlements(self, value):
        self.input_text(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS, value)

    def enter_text_on_leave_entitlements_employee_entitlements(self, value):
        self.input_text(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS, value)

    def enter_text_on_leave_entitlements_my_entitlements(self, value):
        self.input_text(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS, value)

    def enter_text_on_leave_reports_main_menu(self, value):
        self.input_text(self.LEAVE_REPORTS_MAIN_MENU, value)

    def enter_text_on_leave_reports_leave_entitlements_and_usage_report(self, value):
        self.input_text(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, value)

    def enter_text_on_leave_reports_my_leave_entitlements_and_usage_report(self, value):
        self.input_text(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT, value)

    def enter_text_on_leave_configure_main_menu(self, value):
        self.input_text(self.LEAVE_CONFIGURE_MAIN_MENU, value)

    def enter_text_on_leave_configure_leave_period(self, value):
        self.input_text(self.LEAVE_CONFIGURE_LEAVE_PERIOD, value)

    def enter_text_on_leave_configure_leave_types(self, value):
        self.input_text(self.LEAVE_CONFIGURE_LEAVE_TYPES, value)

    def enter_text_on_leave_configure_work_week(self, value):
        self.input_text(self.LEAVE_CONFIGURE_WORK_WEEK, value)

    def enter_text_on_leave_configure_holidays(self, value):
        self.input_text(self.LEAVE_CONFIGURE_HOLIDAYS, value)

    def enter_text_on_leave_leave_list_main_menu(self, value):
        self.input_text(self.LEAVE_LEAVE_LIST_MAIN_MENU, value)

    def enter_text_on_leave_assign_leave_main_menu(self, value):
        self.input_text(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU, value)

    def enter_text_on_time_main_menu(self, value):
        self.input_text(self.TIME_MAIN_MENU, value)

    def enter_text_on_time_timesheets_main_menu(self, value):
        self.input_text(self.TIME_TIMESHEETS_MAIN_MENU, value)

    def enter_text_on_time_timesheets_my_timesheets(self, value):
        self.input_text(self.TIME_TIMESHEETS_MY_TIMESHEETS, value)

    def enter_text_on_time_timesheets_employee_timesheets(self, value):
        self.input_text(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS, value)

    def enter_text_on_time_attendance_main_menu(self, value):
        self.input_text(self.TIME_ATTENDANCE_MAIN_MENU, value)

    def enter_text_on_time_attendance_my_records(self, value):
        self.input_text(self.TIME_ATTENDANCE_MY_RECORDS, value)

    def enter_text_on_time_attendance_punch_in_out(self, value):
        self.input_text(self.TIME_ATTENDANCE_PUNCH_IN_OUT, value)

    def enter_text_on_time_attendance_employee_records(self, value):
        self.input_text(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS, value)

    def enter_text_on_time_attendance_configuration(self, value):
        self.input_text(self.TIME_ATTENDANCE_CONFIGURATION, value)

    def enter_text_on_time_reports_main_menu(self, value):
        self.input_text(self.TIME_REPORTS_MAIN_MENU, value)

    def enter_text_on_time_reports_project_reports(self, value):
        self.input_text(self.TIME_REPORTS_PROJECT_REPORTS, value)

    def enter_text_on_time_reports_employee_reports(self, value):
        self.input_text(self.TIME_REPORTS_EMPLOYEE_REPORTS, value)

    def enter_text_on_time_reports_attendance_summary(self, value):
        self.input_text(self.TIME_REPORTS_ATTENDANCE_SUMMARY, value)

    def enter_text_on_time_project_info_main_menu(self, value):
        self.input_text(self.TIME_PROJECT_INFO_MAIN_MENU, value)

    def enter_text_on_time_project_info_customers(self, value):
        self.input_text(self.TIME_PROJECT_INFO_CUSTOMERS, value)

    def enter_text_on_time_project_info_projects(self, value):
        self.input_text(self.TIME_PROJECT_INFO_PROJECTS, value)

    def enter_text_on_recruitment_main_menu(self, value):
        self.input_text(self.RECRUITMENT_MAIN_MENU, value)

    def enter_text_on_recruitment_candidates_main_menu(self, value):
        self.input_text(self.RECRUITMENT_CANDIDATES_MAIN_MENU, value)

    def enter_text_on_recruitment_vacancies_main_menu(self, value):
        self.input_text(self.RECRUITMENT_VACANCIES_MAIN_MENU, value)

    def enter_text_on_my_info_main_menu(self, value):
        self.input_text(self.MY_INFO_MAIN_MENU, value)

    def enter_text_on_performance_main_menu(self, value):
        self.input_text(self.PERFORMANCE_MAIN_MENU, value)

    def enter_text_on_performance_configure_main_menu(self, value):
        self.input_text(self.PERFORMANCE_CONFIGURE_MAIN_MENU, value)

    def enter_text_on_performance_configure_kpis(self, value):
        self.input_text(self.PERFORMANCE_CONFIGURE_KPIS, value)

    def enter_text_on_performance_configure_trackers(self, value):
        self.input_text(self.PERFORMANCE_CONFIGURE_TRACKERS, value)

    def enter_text_on_performance_manage_reviews_main_menu(self, value):
        self.input_text(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU, value)

    def enter_text_on_performance_manage_reviews_manage_reviews(self, value):
        self.input_text(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS, value)

    def enter_text_on_performance_manage_reviews_my_reviews(self, value):
        self.input_text(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS, value)

    def enter_text_on_performance_manage_reviews_review_list(self, value):
        self.input_text(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST, value)

    def enter_text_on_performance_my_trackers_main_menu(self, value):
        self.input_text(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU, value)

    def enter_text_on_performance_employee_trackers_main_menu(self, value):
        self.input_text(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU, value)

    def enter_text_on_dashboard_main_menu(self, value):
        self.input_text(self.DASHBOARD_MAIN_MENU, value)

    def enter_text_on_directory_main_menu(self, value):
        self.input_text(self.DIRECTORY_MAIN_MENU, value)

    def enter_text_on_maintenance_main_menu(self, value):
        self.input_text(self.MAINTENANCE_MAIN_MENU, value)

    def enter_text_on_maintenance_purge_records_main_menu(self, value):
        self.input_text(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU, value)

    def enter_text_on_maintenance_purge_records_employee_records(self, value):
        self.input_text(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS, value)

    def enter_text_on_maintenance_purge_records_candidate_records(self, value):
        self.input_text(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS, value)

    def enter_text_on_maintenance_access_records_main_menu(self, value):
        self.input_text(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU, value)

    def enter_text_on_buzz_main_menu(self, value):
        self.input_text(self.BUZZ_MAIN_MENU, value)

    def get_admin_main_menu_text(self):
        return self.get_text(self.ADMIN_MAIN_MENU)

    def get_admin_user_management_main_menu_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_MAIN_MENU)

    def get_admin_user_management_users_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_USERS)

    def get_admin_user_management_optional_fields_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_OPTIONAL_FIELDS)

    def get_admin_user_management_custom_fields_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_CUSTOM_FIELDS)

    def get_admin_user_management_data_import_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_DATA_IMPORT)

    def get_admin_user_management_reporting_methods_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_REPORTING_METHODS)

    def get_admin_user_management_termination_reasons_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_TERMINATION_REASONS)

    def get_admin_user_management_my_timesheets_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_MY_TIMESHEETS)

    def get_admin_user_management_employee_timesheets_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_TIMESHEETS)

    def get_admin_user_management_kpis_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_KPIS)

    def get_admin_user_management_trackers_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_TRACKERS)

    def get_admin_user_management_employee_records_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_EMPLOYEE_RECORDS)

    def get_admin_user_management_candidate_records_text(self):
        return self.get_text(self.ADMIN_USER_MANAGEMENT_CANDIDATE_RECORDS)

    def get_admin_job_main_menu_text(self):
        return self.get_text(self.ADMIN_JOB_MAIN_MENU)

    def get_admin_job_job_titles_text(self):
        return self.get_text(self.ADMIN_JOB_JOB_TITLES)

    def get_admin_job_pay_grades_text(self):
        return self.get_text(self.ADMIN_JOB_PAY_GRADES)

    def get_admin_job_employment_status_text(self):
        return self.get_text(self.ADMIN_JOB_EMPLOYMENT_STATUS)

    def get_admin_job_job_categories_text(self):
        return self.get_text(self.ADMIN_JOB_JOB_CATEGORIES)

    def get_admin_job_work_shifts_text(self):
        return self.get_text(self.ADMIN_JOB_WORK_SHIFTS)

    def get_admin_job_my_records_text(self):
        return self.get_text(self.ADMIN_JOB_MY_RECORDS)

    def get_admin_job_punch_in_out_text(self):
        return self.get_text(self.ADMIN_JOB_PUNCH_IN_OUT)

    def get_admin_job_employee_records_text(self):
        return self.get_text(self.ADMIN_JOB_EMPLOYEE_RECORDS)

    def get_admin_job_configuration_text(self):
        return self.get_text(self.ADMIN_JOB_CONFIGURATION)

    def get_admin_job_manage_reviews_text(self):
        return self.get_text(self.ADMIN_JOB_MANAGE_REVIEWS)

    def get_admin_job_my_reviews_text(self):
        return self.get_text(self.ADMIN_JOB_MY_REVIEWS)

    def get_admin_job_review_list_text(self):
        return self.get_text(self.ADMIN_JOB_REVIEW_LIST)

    def get_admin_organization_main_menu_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_MAIN_MENU)

    def get_admin_organization_general_information_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_GENERAL_INFORMATION)

    def get_admin_organization_locations_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_LOCATIONS)

    def get_admin_organization_structure_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_STRUCTURE)

    def get_admin_organization_add_entitlements_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_ADD_ENTITLEMENTS)

    def get_admin_organization_employee_entitlements_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_EMPLOYEE_ENTITLEMENTS)

    def get_admin_organization_my_entitlements_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_MY_ENTITLEMENTS)

    def get_admin_organization_project_reports_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_PROJECT_REPORTS)

    def get_admin_organization_employee_reports_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_EMPLOYEE_REPORTS)

    def get_admin_organization_attendance_summary_text(self):
        return self.get_text(self.ADMIN_ORGANIZATION_ATTENDANCE_SUMMARY)

    def get_admin_qualifications_main_menu_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_MAIN_MENU)

    def get_admin_qualifications_skills_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_SKILLS)

    def get_admin_qualifications_education_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_EDUCATION)

    def get_admin_qualifications_licenses_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_LICENSES)

    def get_admin_qualifications_languages_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_LANGUAGES)

    def get_admin_qualifications_memberships_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_MEMBERSHIPS)

    def get_admin_qualifications_leave_entitlements_and_usage_report_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def get_admin_qualifications_my_leave_entitlements_and_usage_report_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def get_admin_qualifications_customers_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_CUSTOMERS)

    def get_admin_qualifications_projects_text(self):
        return self.get_text(self.ADMIN_QUALIFICATIONS_PROJECTS)

    def get_admin_nationalities_main_menu_text(self):
        return self.get_text(self.ADMIN_NATIONALITIES_MAIN_MENU)

    def get_admin_nationalities_leave_period_text(self):
        return self.get_text(self.ADMIN_NATIONALITIES_LEAVE_PERIOD)

    def get_admin_nationalities_leave_types_text(self):
        return self.get_text(self.ADMIN_NATIONALITIES_LEAVE_TYPES)

    def get_admin_nationalities_work_week_text(self):
        return self.get_text(self.ADMIN_NATIONALITIES_WORK_WEEK)

    def get_admin_nationalities_holidays_text(self):
        return self.get_text(self.ADMIN_NATIONALITIES_HOLIDAYS)

    def get_admin_corporate_branding_main_menu_text(self):
        return self.get_text(self.ADMIN_CORPORATE_BRANDING_MAIN_MENU)

    def get_admin_configuration_main_menu_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_MAIN_MENU)

    def get_admin_configuration_email_configuration_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_EMAIL_CONFIGURATION)

    def get_admin_configuration_email_subscriptions_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_EMAIL_SUBSCRIPTIONS)

    def get_admin_configuration_localization_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_LOCALIZATION)

    def get_admin_configuration_language_packages_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_LANGUAGE_PACKAGES)

    def get_admin_configuration_modules_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_MODULES)

    def get_admin_configuration_social_media_authentication_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_SOCIAL_MEDIA_AUTHENTICATION)

    def get_admin_configuration_register_oauth_client_text(self):
        return self.get_text(self.ADMIN_CONFIGURATION_REGISTER_OAUTH_CLIENT)

    def get_pim_main_menu_text(self):
        return self.get_text(self.PIM_MAIN_MENU)

    def get_pim_configuration_main_menu_text(self):
        return self.get_text(self.PIM_CONFIGURATION_MAIN_MENU)

    def get_pim_configuration_optional_fields_text(self):
        return self.get_text(self.PIM_CONFIGURATION_OPTIONAL_FIELDS)

    def get_pim_configuration_custom_fields_text(self):
        return self.get_text(self.PIM_CONFIGURATION_CUSTOM_FIELDS)

    def get_pim_configuration_data_import_text(self):
        return self.get_text(self.PIM_CONFIGURATION_DATA_IMPORT)

    def get_pim_configuration_reporting_methods_text(self):
        return self.get_text(self.PIM_CONFIGURATION_REPORTING_METHODS)

    def get_pim_configuration_termination_reasons_text(self):
        return self.get_text(self.PIM_CONFIGURATION_TERMINATION_REASONS)

    def get_pim_employee_list_main_menu_text(self):
        return self.get_text(self.PIM_EMPLOYEE_LIST_MAIN_MENU)

    def get_pim_add_employee_main_menu_text(self):
        return self.get_text(self.PIM_ADD_EMPLOYEE_MAIN_MENU)

    def get_pim_reports_main_menu_text(self):
        return self.get_text(self.PIM_REPORTS_MAIN_MENU)

    def get_leave_main_menu_text(self):
        return self.get_text(self.LEAVE_MAIN_MENU)

    def get_leave_apply_main_menu_text(self):
        return self.get_text(self.LEAVE_APPLY_MAIN_MENU)

    def get_leave_my_leave_main_menu_text(self):
        return self.get_text(self.LEAVE_MY_LEAVE_MAIN_MENU)

    def get_leave_entitlements_main_menu_text(self):
        return self.get_text(self.LEAVE_ENTITLEMENTS_MAIN_MENU)

    def get_leave_entitlements_add_entitlements_text(self):
        return self.get_text(self.LEAVE_ENTITLEMENTS_ADD_ENTITLEMENTS)

    def get_leave_entitlements_employee_entitlements_text(self):
        return self.get_text(self.LEAVE_ENTITLEMENTS_EMPLOYEE_ENTITLEMENTS)

    def get_leave_entitlements_my_entitlements_text(self):
        return self.get_text(self.LEAVE_ENTITLEMENTS_MY_ENTITLEMENTS)

    def get_leave_reports_main_menu_text(self):
        return self.get_text(self.LEAVE_REPORTS_MAIN_MENU)

    def get_leave_reports_leave_entitlements_and_usage_report_text(self):
        return self.get_text(self.LEAVE_REPORTS_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def get_leave_reports_my_leave_entitlements_and_usage_report_text(self):
        return self.get_text(self.LEAVE_REPORTS_MY_LEAVE_ENTITLEMENTS_AND_USAGE_REPORT)

    def get_leave_configure_main_menu_text(self):
        return self.get_text(self.LEAVE_CONFIGURE_MAIN_MENU)

    def get_leave_configure_leave_period_text(self):
        return self.get_text(self.LEAVE_CONFIGURE_LEAVE_PERIOD)

    def get_leave_configure_leave_types_text(self):
        return self.get_text(self.LEAVE_CONFIGURE_LEAVE_TYPES)

    def get_leave_configure_work_week_text(self):
        return self.get_text(self.LEAVE_CONFIGURE_WORK_WEEK)

    def get_leave_configure_holidays_text(self):
        return self.get_text(self.LEAVE_CONFIGURE_HOLIDAYS)

    def get_leave_leave_list_main_menu_text(self):
        return self.get_text(self.LEAVE_LEAVE_LIST_MAIN_MENU)

    def get_leave_assign_leave_main_menu_text(self):
        return self.get_text(self.LEAVE_ASSIGN_LEAVE_MAIN_MENU)

    def get_time_main_menu_text(self):
        return self.get_text(self.TIME_MAIN_MENU)

    def get_time_timesheets_main_menu_text(self):
        return self.get_text(self.TIME_TIMESHEETS_MAIN_MENU)

    def get_time_timesheets_my_timesheets_text(self):
        return self.get_text(self.TIME_TIMESHEETS_MY_TIMESHEETS)

    def get_time_timesheets_employee_timesheets_text(self):
        return self.get_text(self.TIME_TIMESHEETS_EMPLOYEE_TIMESHEETS)

    def get_time_attendance_main_menu_text(self):
        return self.get_text(self.TIME_ATTENDANCE_MAIN_MENU)

    def get_time_attendance_my_records_text(self):
        return self.get_text(self.TIME_ATTENDANCE_MY_RECORDS)

    def get_time_attendance_punch_in_out_text(self):
        return self.get_text(self.TIME_ATTENDANCE_PUNCH_IN_OUT)

    def get_time_attendance_employee_records_text(self):
        return self.get_text(self.TIME_ATTENDANCE_EMPLOYEE_RECORDS)

    def get_time_attendance_configuration_text(self):
        return self.get_text(self.TIME_ATTENDANCE_CONFIGURATION)

    def get_time_reports_main_menu_text(self):
        return self.get_text(self.TIME_REPORTS_MAIN_MENU)

    def get_time_reports_project_reports_text(self):
        return self.get_text(self.TIME_REPORTS_PROJECT_REPORTS)

    def get_time_reports_employee_reports_text(self):
        return self.get_text(self.TIME_REPORTS_EMPLOYEE_REPORTS)

    def get_time_reports_attendance_summary_text(self):
        return self.get_text(self.TIME_REPORTS_ATTENDANCE_SUMMARY)

    def get_time_project_info_main_menu_text(self):
        return self.get_text(self.TIME_PROJECT_INFO_MAIN_MENU)

    def get_time_project_info_customers_text(self):
        return self.get_text(self.TIME_PROJECT_INFO_CUSTOMERS)

    def get_time_project_info_projects_text(self):
        return self.get_text(self.TIME_PROJECT_INFO_PROJECTS)

    def get_recruitment_main_menu_text(self):
        return self.get_text(self.RECRUITMENT_MAIN_MENU)

    def get_recruitment_candidates_main_menu_text(self):
        return self.get_text(self.RECRUITMENT_CANDIDATES_MAIN_MENU)

    def get_recruitment_vacancies_main_menu_text(self):
        return self.get_text(self.RECRUITMENT_VACANCIES_MAIN_MENU)

    def get_my_info_main_menu_text(self):
        return self.get_text(self.MY_INFO_MAIN_MENU)

    def get_performance_main_menu_text(self):
        return self.get_text(self.PERFORMANCE_MAIN_MENU)

    def get_performance_configure_main_menu_text(self):
        return self.get_text(self.PERFORMANCE_CONFIGURE_MAIN_MENU)

    def get_performance_configure_kpis_text(self):
        return self.get_text(self.PERFORMANCE_CONFIGURE_KPIS)

    def get_performance_configure_trackers_text(self):
        return self.get_text(self.PERFORMANCE_CONFIGURE_TRACKERS)

    def get_performance_manage_reviews_main_menu_text(self):
        return self.get_text(self.PERFORMANCE_MANAGE_REVIEWS_MAIN_MENU)

    def get_performance_manage_reviews_manage_reviews_text(self):
        return self.get_text(self.PERFORMANCE_MANAGE_REVIEWS_MANAGE_REVIEWS)

    def get_performance_manage_reviews_my_reviews_text(self):
        return self.get_text(self.PERFORMANCE_MANAGE_REVIEWS_MY_REVIEWS)

    def get_performance_manage_reviews_review_list_text(self):
        return self.get_text(self.PERFORMANCE_MANAGE_REVIEWS_REVIEW_LIST)

    def get_performance_my_trackers_main_menu_text(self):
        return self.get_text(self.PERFORMANCE_MY_TRACKERS_MAIN_MENU)

    def get_performance_employee_trackers_main_menu_text(self):
        return self.get_text(self.PERFORMANCE_EMPLOYEE_TRACKERS_MAIN_MENU)

    def get_dashboard_main_menu_text(self):
        return self.get_text(self.DASHBOARD_MAIN_MENU)

    def get_directory_main_menu_text(self):
        return self.get_text(self.DIRECTORY_MAIN_MENU)

    def get_maintenance_main_menu_text(self):
        return self.get_text(self.MAINTENANCE_MAIN_MENU)

    def get_maintenance_purge_records_main_menu_text(self):
        return self.get_text(self.MAINTENANCE_PURGE_RECORDS_MAIN_MENU)

    def get_maintenance_purge_records_employee_records_text(self):
        return self.get_text(self.MAINTENANCE_PURGE_RECORDS_EMPLOYEE_RECORDS)

    def get_maintenance_purge_records_candidate_records_text(self):
        return self.get_text(self.MAINTENANCE_PURGE_RECORDS_CANDIDATE_RECORDS)

    def get_maintenance_access_records_main_menu_text(self):
        return self.get_text(self.MAINTENANCE_ACCESS_RECORDS_MAIN_MENU)

    def get_buzz_main_menu_text(self):
        return self.get_text(self.BUZZ_MAIN_MENU)
