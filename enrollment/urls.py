from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^section/list/details$', views.sectionDetails, name = 'section-details'),
        url(r'^$', views.index, name = 'reg-index'),
        #-----------------------CURRICULUM---------------------------------------------------------
        url(r'^curriculum-list/$', views.curriculumList, name = 'curriculum-list'),
        url(r'^curriculum-list/table$', views.tableCurriculumList, name = 'curriculum-table'),
        url(r'^curriculum-list/add$', views.addCurriculumProfile, name = 'curriculum-add'),
        url(r'^curriculum-list/create/(?P<pk>\d+)$', views.createCurriculumProfile, name = 'curriculum-create'),
        #CURR DETAIL
        url(r'^curriculum-list/(?P<pk>\d+)/$', views.curriculumDetails, name = 'curriculum-detail'),
        url(r'^curriculum-list/subject-table/(?P<pk>\d+)$', views.tableCurriculumSubjectList, name = 'subject-table'),
        url(r'^curriculum-list/subject/add/(?P<pk>\d+)$', views.openCurriculumSubjectAdd, name = 'subject-add'),
        
        url(r'^curriculum-list/subject/edit/(?P<pk>\d+)$', views.editSubject, name = 'subject-edit'),
        url(r'^curriculum-list/subject/edit-form/(?P<pk>\d+)$', views.form_editSubject, name = 'subject-edit-form'),
        #-----------------------SECTION------------------------------------------------------------
        url(r'^section-list$', views.sectionList, name = 'section-list'),
        url(r'^section-list/table$', views.sectionTable, name = 'section-table'),
        url(r'^section-list/add$', views.addSection, name = 'section-create'),
        url(r'^section-list/add-form$', views.generateSectionForm, name = 'section-create-form'),
        
        url(r'^section-list/edit/(?P<pk>\d+)$', views.editSection, name = 'section-edit'),
        url(r'^section-list/edit-form/(?P<pk>\d+)$', views.form_editSection, name = 'section-edit-form'),
        
        url(r'^section-list/(?P<pk>\d+)/$', views.sectionDetails, name = 'section-detail'),
        url(r'^section-list/detail-table/(?P<pk>\d+)$', views.tableSectionDetail, name = 'section-detail-table'),
        url(r'^section-list/section-detail-add/(?P<pk>\d+)$', views.sectionDetailAdd, name = 'section-detail-add'),
        url(r'^section-list/section-detail-form/(?P<pk>\d+)$', views.sectionDetailForm, name = 'section-detail-form'),
        url(r'^student-names/$', views.studentNames, name = 'student-names'),
        
        #-----------------------SCHOLARSHIP--------------------------------------------------------
        url(r'^scholarship-list/$', views.scholarshipList, name = 'scholarship-list'),
        url(r'^scholarship-list/table$', views.tableScholarshipList, name = 'scholarship-table'),
        url(r'^scholarship-list/add$', views.addScholarshipProfile, name = 'scholarship-add'),
        url(r'^scholarship-list/create$', views.createScholarshipProfile, name = 'scholarship-create'),
        
        url(r'^scholarship-list/update/(?P<pk>\d+)$', views.updateScholarship, name = 'scholarship-update'),
        url(r'^scholarship-list/edit-form/(?P<pk>\d+)$', views.editScholarshipForm, name = 'scholarship-edit-form'),

        url(r'^scholars-list/(?P<pk>\d+)$', views.scholarList, name = 'scholar-list'),
        url(r'^scholars-list/table/(?P<pk>\d+)$', views.scholarTable, name = 'table-scholar-list'),
        #-----------------------SUBJECT OFFERING----------------------------------------------------
       
        url(r'^subjectOffering-list/(?P<pk>\d+)$', views.subjectOfferingList, name = 'subjectOffering-list'),
        url(r'^subjectOffering-list/table/(?P<pk>\d+)$', views.tableSubjectOfferingList, name = 'subjectOffering-table'),
        url(r'^subjectOffering-list/add/(?P<pk>\d+)$', views.addSubjectOfferingProfile, name = 'subjectOffering-add'),
        url(r'^subjectOffering-list/create/(?P<pk>\d+)$', views.createSubjectOfferingProfile, name = 'subjectOffering-create'),
        url(r'^subjectOffering-list/(?P<pk>\d+)/$', views.subjectOfferingDetail, name = 'subjectOffering-detail'),
        
        url(r'^subjectOffering-list/update/(?P<pk>\d+)$', views.updateSubjectOffering, name = 'subjectOffering-update'),
        url(r'^subjectOffering-list/edit-form/(?P<pk>\d+)$', views.editSubjectOfferingForm, name = 'subjectOffering-edit-form'),
        #-----------------------SCHOOL YEAR----------------------------------------------------
        url(r'^school-year-list$', views.schoolYearList, name = 'school-year-list'),
        url(r'^school-year-list/table$', views.tableSchoolYearList, name = 'school-year-table'),
        url(r'^school-year-list/add$', views.createSchoolYear, name = 'school-year-create'),
        url(r'^school-year-list/add-form$', views.form_createSchoolYear, name = 'school-year-create-form'),
        
        url(r'^school-year-list/update/(?P<pk>\d+)$', views.editSchoolYear, name = 'school-year-edit'),
        url(r'^school-year-list/edit-form/(?P<pk>\d+)$', views.form_editSchoolYear, name = 'school-year-edit-form'),
        
        url(r'^school-year-list/delete/(?P<pk>\d+)$', views.deleteSchoolYear, name = 'school-year-delete'),
        url(r'^school-year-list/delete-form/(?P<pk>\d+)$', views.form_deleteSchoolYear, name = 'school-year-delete-form'),
        #-----------------------YEAR LEVEL----------------------------------------------------
        url(r'^year-level-list$', views.yearLevelList, name = 'year-level-list'),
        url(r'^year-level-list/table$', views.tableYearLevelList, name = 'year-level-table'),
        
        url(r'^year-level-list/add$', views.createYearLevel, name = 'year-level-create'),
        url(r'^year-level-list/add-form$', views.form_createYearLevel, name = 'year-level-create-form'),
        
        url(r'^year-level-list/update/(?P<pk>\d+)$', views.editYearLevel, name = 'year-level-list-update'),
        url(r'^year-level-list/edit-form/(?P<pk>\d+)$', views.form_editYearLevel, name = 'year-level-edit-form'),
        
        url(r'^year-level-list/delete/(?P<pk>\d+)$', views.delete_yearLevel, name = 'year-level-delete'),
    ]

urlpatterns += [
    url(r'^subject/delete$', views.deleteSubj, name = 'delete-subject'),
]

''' URL DUMP

#url(r'^curriculum-list/update/(?P<pk>\d+)$', views.updateCurriculum, name = 'curriculum-update'),
#url(r'^curriculum-list/edit-form/(?P<pk>\d+)$', views.editCurriculumForm, name = 'curriculum-edit-form'),
#url(r'^school-year/create$', views.newSchoolYear, name = 'create-schoolyear'),
'''