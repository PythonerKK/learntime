from django.urls import path

from learntime.student import views
from learntime.student.views import (StudentExcelImportView, StudentExcelExportView, StudentBulkDeleteView, \
                                     StudentAllDeleteView, StudentCreditView, StudentEditCreditView,
                                     StudentBulkAddCreditView, StudentCreditApplyListView, StudentCreditExcelImportView,
                                     StudentCreditVerifyListView)

app_name = "students"
urlpatterns = [

    path('', view=views.StudentList.as_view(), name='students'),
    path('student-detail/<int:pk>/', view=views.StudentDetail.as_view(), name='student_detail'),
    path('student-create/', view=views.StudentCreate.as_view(), name='student_create'),
    path('student-update/<int:pk>/', view=views.StudentUpdate.as_view(), name='student_update'),
    path("student-delete/<int:pk>/", view=views.StudentDelete.as_view(), name='student_delete'),

    # 导入学生接口
    path("student-import/", view=StudentExcelImportView.as_view(), name='student_import'),
    # 导出学生接口
    path("student-export/", view=StudentExcelExportView.as_view(), name='student_export'),

    # 学生批量删除接口
    path("student-bulk-delete/", view=StudentBulkDeleteView.as_view(), name='student_bulk_delete'),
    # 学生全部删除
    path("student-all-delete/", view=StudentAllDeleteView.as_view(), name='student_all_delete'),

    # 学时管理页
    path("credit/", view=StudentCreditView.as_view(), name='student_credit'),
    # 学时修改接口
    path("edit-credit/", view=StudentEditCreditView.as_view(), name='student_credit_edit'),
    # 学时批量增加接口
    path("bulk-add-credit/", view=StudentBulkAddCreditView.as_view(), name='student_credit_add'),

    # 申请增加学时列表页
    path('student-credit-apply/', view=StudentCreditApplyListView.as_view(), name='student_credit_apply'),
    # 审核加学时
    path('student-credit-verify/', view=StudentCreditVerifyListView.as_view(), name='student_credit_verify'),
    # 导入需要增加学时的学生文件接口
    path("student-credit-import/", view=StudentCreditExcelImportView.as_view(), name='student_credit_import'),
]
