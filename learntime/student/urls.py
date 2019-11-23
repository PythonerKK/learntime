from django.urls import path

from learntime.student import views
from learntime.student.views import StudentExcelImportView, StudentExcelExportView, StudentBulkDeleteView, \
    StudentAllDeleteView, StudentCreditView, StudentEditCreditView

app_name = "students"
urlpatterns = [

    path('', view=views.StudentList.as_view(), name='students'),
    path('student-detail/<int:pk>/', view=views.StudentDetail.as_view(), name='student_detail'),
    path('student-create/', view=views.StudentCreate.as_view(), name='student_create'),
    path('student-update/<int:pk>/', view=views.StudentUpdate.as_view(), name='student_update'),
    path("student-delete/<int:pk>/", view=views.StudentDelete.as_view(), name='student_delete'),

    path("student-import/", view=StudentExcelImportView.as_view(), name='student_import'),
    path("student-export/", view=StudentExcelExportView.as_view(), name='student_export'),

    path("student-bulk-delete/", view=StudentBulkDeleteView.as_view(), name='student_bulk_delete'),
    path("student-all-delete/", view=StudentAllDeleteView.as_view(), name='student_all_delete'),

    # 学生学时管理
    path("credit/", view=StudentCreditView.as_view(), name='student_credit'),
    path("edit-credit/", view=StudentEditCreditView.as_view(), name='student_credit_edit')
    # path('admin-delete/<int:pk>/', view=AdminDeleteView.as_view(), name='admin_delete'),
    # path("apply_comfirm/", view=ApplyConfirmView.as_view(), name="apply_comfirm"),
    # path("update_profile/<int:pk>/", view=AdminUpdateView.as_view(), name="update_profile")
]
