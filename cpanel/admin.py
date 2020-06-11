from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


admin.site.register(Stakeholders)
admin.site.register(StakeholdersPhones)
admin.site.register(StakeholdersAddress)
admin.site.register(Patient)
admin.site.register(PatientRelativesPhones)
admin.site.register(Physician)
admin.site.register(Nurse)
admin.site.register(NurseSpecialization)
admin.site.register(Paramedic)
admin.site.register(Specialist)
admin.site.register(SpecialistSpecialization)
admin.site.register(Pharmacist)
admin.site.register(PharmacistSpecialization)
admin.site.register(MedicalInstitutions)
admin.site.register(MedicalInstitutionsPhone)
admin.site.register(MedicalInstitutionsAddress)
admin.site.register(Labs)
admin.site.register(LabsAnalysisAndRadiology)
admin.site.register(Clinic)
admin.site.register(Pharmacy)
admin.site.register(Hospital)
admin.site.register(InsuranceCompanies)
admin.site.register(InsuranceCompaniesPhone)
admin.site.register(InsuranceCompaniesAddress)
admin.site.register(InsuranceTypes)
admin.site.register(Specialization)
admin.site.register(PatientHistory)
admin.site.register(PhysicianPatientAppointment)
admin.site.register(PhysicianHospitalWorkingTime)
admin.site.register(PhysicianClinicWorkingTime)
admin.site.register(PhysicianRating)
admin.site.register(LabRating)
admin.site.register(ClinicRating)
admin.site.register(HospitalRating)
admin.site.register(HospitalNurses)
admin.site.register(ClinicNurses)
admin.site.register(LabNurses)
admin.site.register(LabSpecialists)
admin.site.register(HospitalSpecialists)
admin.site.register(ClinicSpecialists)
admin.site.register(PharmacyPharmacists)
admin.site.register(PhysicianSpecialization)
admin.site.register(HospitalSpecialization)
admin.site.register(ClinicSpecialization)
admin.site.register(LabsInsuranceDeals)
admin.site.register(ClinicsInsuranceDeals)
admin.site.register(HospitalInsuranceDeals)
admin.site.register(PharmacyInsuranceDeals)
admin.site.register(PatientInsurance)
