
from django.db import models
from scrap import models as scrap_models
"""
-------------------------------------------------
        @@ MODELS FOR ALL INDIA GOVT JobDetails @@    ||
-------------------------------------------------
"""

class UpscJobDetails(models.Model):
    upsc_details_id = models.AutoField(primary_key=True)
    upsc            = models.OneToOneField(scrap_models.UpscJobs,on_delete=models.CASCADE,related_name='upsc_details')
    more_info       = models.TextField()
    join_id         = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Upsc JobDetails"

class SscJobDetails(models.Model):
    ssc_details_id = models.AutoField(primary_key=True)
    ssc            = models.OneToOneField(scrap_models.SscJobs,on_delete=models.CASCADE,related_name='ssc_details')
    more_info      = models.TextField()
    join_id        = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Ssc JobDetails"

class OtherAllIndiaJobDetails(models.Model):
    other_all_india_details_id = models.AutoField(primary_key=True)
    other_all_india            = models.OneToOneField(scrap_models.OtherAllIndiaJobs,on_delete=models.CASCADE,related_name='all_india_details')
    more_info                  = models.TextField()
    join_id                    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Other All India JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE GOVT JobDetails @@    ||
-------------------------------------------------
"""


class OdishaGovtJobDetails(models.Model):
    odisha_details_id = models.AutoField(primary_key=True)
    odisha            = models.OneToOneField(scrap_models.OdishaGovtJobs,on_delete=models.CASCADE,related_name='odisha_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Odisha Govt JobDetails"

class AndamanNicoborGovtJobDetails(models.Model):
    andaman_details_id = models.AutoField(primary_key=True)
    andaman            = models.OneToOneField(scrap_models.AndamanNicoborGovtJobs,on_delete=models.CASCADE,related_name='andaman_details')
    more_info          = models.TextField()
    join_id            = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Govt JobDetails"

class AndhraPradeshGovtJobDetails(models.Model):
    andhra_id         = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Govt JobDetails"

class ArunachalPradeshGovernmentJobDetails(models.Model):
    arunachal_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Govt JobDetails"

class AssamGovtJobDetails(models.Model):
    assam_id          = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Govt JobDetails"

class BiharGovtJobDetails(models.Model):
    bihar_id          = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Govt JobDetails"

class ChandigarhGovtJobDetails(models.Model):
    chandigarh_id     = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Govt JobDetails"

class ChhattisgarhGovtJobDetails(models.Model):
    chhattisgarh_id   = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Govt JobDetails"

class DadraNagarHaveliGovtJobDetails(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    more_info             = models.TextField()
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Govt JobDetails"

class DamanDiuGovtJobDetails(models.Model):
    daman_diu_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Govt JobDetails"

class DelhiGovtJobDetails(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Govt JobDetails"

class GoaGovernmentJobDetails(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Govt JobDetails"

class GujuratGovtJobDetails(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Govt JobDetails"

class HaryanaGovtJobDetails(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Govt JobDetails"

class HimachalPradeshGovtJobDetails(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Govt JobDetails"

class JammuKashmirGovtJobDetails(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Govt JobDetails"

class JharkhandGovtJobDetails(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Govt JobDetails"

class KarnatakaGovtJobDetails(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Govt JobDetails"

class KeralaGovtJobDetails(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Govt JobDetails"

class LakshadweepGovernmentJobDetails(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Govt JobDetails"

class MadhyaPradeshGovtJobDetails(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Govt JobDetails"

class MaharashtraGovtJobDetails(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Govt JobDetails"

class ManipurGovtJobDetails(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Govt JobDetails"

class MeghalayaGovtJobDetails(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Govt JobDetails"

class MizoramGovtJobDetails(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Govt JobDetails"

class NagalandGovtJobDetails(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Govt JobDetails"

class PuduchheryGovtJobDetails(models.Model):
    puduchhery_id     = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Govt JobDetails"

class PunjabGovernmentJobDetails(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Govt JobDetails"

class RajasthanGovtJobDetails(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Govt JobDetails"

class SikkimGovtJobDetails(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Govt JobDetails"

class TamilGovtJobDetails(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Govt JobDetails"

class TelanganaGovtJobDetails(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Govt JobDetails"

class TripuraGovtJobDetails(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Govt JobDetails"

class UttarakhandGovtJobDetails(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Govt JobDetails"

class UttarPradeshGovtJobDetails(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Govt JobDetails"

class WestBengalGovtJobDetails(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Govt JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR BANK AND OTHER FINANCIAL JobDetails @@    ||
-------------------------------------------------
"""

class AllBankJobDetails(models.Model):
    bankJobDetails_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    bank_name         = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "All Bank JobDetails"


class OtherFinancialJobDetails(models.Model):
    financialJobDetails_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Other Financial JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE TEACHING JobDetails @@    ||
-------------------------------------------------
"""


class AllIndiaTeachingJobDetails(models.Model):
    all_india_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Teaching JobDetails"

class AndamanNicoborTeachingJobDetails(models.Model):
    andaman_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Teaching JobDetails"

class AndhraPradeshTeachingJobDetails(models.Model):
    andhra_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Teaching JobDetails"

class ArunachalPradeshTeachingJobDetails(models.Model):
    arunachal_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Teaching JobDetails"

class AssamTeachingJobDetails(models.Model):
    assam_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Teaching JobDetails"

class BiharTeachingJobDetails(models.Model):
    bihar_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Teaching JobDetails"

class ChandigarhTeachingJobDetails(models.Model):
    chandigarh_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Teaching JobDetails"

class ChhattisgarhTeachingJobDetails(models.Model):
    chhattisgarh_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Teaching JobDetails"

class DadraNagarHaveliTeachingJobDetails(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    start_date            = models.CharField(max_length=60)
    last_date             = models.CharField(max_length=60)
    post_name             = models.CharField(max_length=255)
    education             = models.CharField(max_length=255)
    more_info             = models.TextField()
    requirement_board     = models.CharField(max_length=255)
    type                  = models.IntegerField()
    job_id                = models.IntegerField(default=None,blank=True,null=True)
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Teaching JobDetails"

class DamanDiuTeachingJobDetails(models.Model):
    DamanDiuTeachingJobDetails      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Teaching JobDetails"

class DelhiTeachingJobDetails(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Teaching JobDetails"

class GoaTeachingJobDetails(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Teaching JobDetails"

class GujuratTeachingJobDetails(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Teaching JobDetails"

class HaryanaTeachingJobDetails(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Teaching JobDetails"

class HimachalPradeshTeachingJobDetails(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Teaching JobDetails"

class JammuKashmirTeachingJobDetails(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Teaching JobDetails"

class JharkhandTeachingJobDetails(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Teaching JobDetails"

class KarnatakaTeachingJobDetails(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Teaching JobDetails"

class KeralaTeachingJobDetails(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Teaching JobDetails"

class LakshadweepTeachingJobDetails(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Teaching JobDetails"

class MadhyaPradeshTeachingJobDetails(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Teaching JobDetails"

class MaharashtraTeachingJobDetails(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Teaching JobDetails"

class ManipurTeachingJobDetails(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Teaching JobDetails"

class MeghalayaTeachingJobDetails(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Teaching JobDetails"

class MizoramTeachingJobDetails(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Teaching JobDetails"

class NagalandTeachingJobDetails(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Teaching JobDetails"

class OdishaTeachingJobDetails(models.Model):
    puduchhery_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Teaching JobDetails"

class PuduchheryTeachingJobDetails(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching JobDetails"

class PunjabTeachingJobDetails(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching JobDetails"

class RajasthanTeachingJobDetails(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Teaching JobDetails"

class SikkimTeachingJobDetails(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Teaching JobDetails"

class TamilNaduTeachingJobDetails(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Teaching JobDetails"

class TelanganaTeachingJobDetails(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Teaching JobDetails"

class TripuraTeachingJobDetails(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Teaching JobDetails"

class UttarakhandTeachingJobDetails(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Teaching JobDetails"

class UttarPradeshTeachingJobDetails(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Teaching JobDetails"

class WestBengalTeachingJobDetails(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Teaching JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE ENGINEERING JobDetails @@    ||
-------------------------------------------------
"""


class AllIndiaEnggJobDetails(models.Model):
    all_india_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Engg JobDetails"


class AllIndiaFellowEnggJobDetails(models.Model):
    all_india_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Fellow Engg JobDetails"

class AndamanNicoborEnggJobDetails(models.Model):
    andaman_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Engg JobDetails"

class AndhraPradeshEnggJobDetails(models.Model):
    andhra_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Engg JobDetails"

class ArunachalPradeshEnggJobDetails(models.Model):
    arunachal_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Engg JobDetails"

class AssamEnggJobDetails(models.Model):
    assam_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Engg JobDetails"

class BiharEnggJobDetails(models.Model):
    bihar_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Engg JobDetails"

class ChandigarhEnggJobDetails(models.Model):
    chandigarh_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Engg JobDetails"

class ChhattisgarhEnggJobDetails(models.Model):
    chhattisgarh_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Engg JobDetails"

class DadraNagarHaveliEnggJobDetails(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    start_date            = models.CharField(max_length=60)
    last_date             = models.CharField(max_length=60)
    post_name             = models.CharField(max_length=255)
    education             = models.CharField(max_length=255)
    more_info             = models.TextField()
    requirement_board     = models.CharField(max_length=255)
    type                  = models.IntegerField()
    job_id                = models.IntegerField(default=None,blank=True,null=True)
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Engg JobDetails"

class DamanDiuEnggJobDetails(models.Model):
    DamanDiuEnggJobDetails      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Engg JobDetails"

class DelhiEnggJobDetails(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Engg JobDetails"

class GoaEnggJobDetails(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Engg JobDetails"

class GujuratEnggJobDetails(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Engg JobDetails"

class HaryanaEnggJobDetails(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Engg JobDetails"

class HimachalPradeshEnggJobDetails(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Engg JobDetails"

class JammuKashmirEnggJobDetails(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Engg JobDetails"

class JharkhandEnggJobDetails(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Engg JobDetails"

class KarnatakaEnggJobDetails(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Engg JobDetails"

class KeralaEnggJobDetails(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Engg JobDetails"

class LakshadweepEnggJobDetails(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Engg JobDetails"

class MadhyaPradeshEnggJobDetails(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Engg JobDetails"

class MaharashtraEnggJobDetails(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Engg JobDetails"

class ManipurEnggJobDetails(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Engg JobDetails"

class MeghalayaEnggJobDetails(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Engg JobDetails"

class MizoramEnggJobDetails(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Engg JobDetails"

class NagalandEnggJobDetails(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Engg JobDetails"

class OdishaEnggJobDetails(models.Model):
    puduchhery_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Engg JobDetails"

class PuduchheryEnggJobDetails(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg JobDetails"

class PunjabEnggJobDetails(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg JobDetails"

class RajasthanEnggJobDetails(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Engg JobDetails"

class SikkimEnggJobDetails(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Engg JobDetails"

class TamilNaduEnggJobDetails(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Engg JobDetails"

class TelanganaEnggJobDetails(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Engg JobDetails"

class TripuraEnggJobDetails(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Engg JobDetails"

class UttarakhandEnggJobDetails(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Engg JobDetails"

class UttarPradeshEnggJobDetails(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Engg JobDetails"

class WestBengalEnggJobDetails(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Engg JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR RAILWAY JobDetails @@    ||
-------------------------------------------------
"""


class RailwayJob(models.Model):
    railway_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Railway JobDetails JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR POLICE AND DEFENCE JobDetails @@    ||
-------------------------------------------------
"""

class StatewisePoliceJobDetails(models.Model):
    statewise_police_id = models.AutoField(primary_key=True)
    start_date          = models.CharField(max_length=60)
    last_date           = models.CharField(max_length=60)
    post_name           = models.CharField(max_length=255)
    education           = models.CharField(max_length=255)
    more_info           = models.TextField()
    requirement_board   = models.CharField(max_length=255)
    type                = models.IntegerField()
    job_id              = models.IntegerField(default=None,blank=True,null=True)
    join_id             = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Statewise Police JobDetails"

class PoliceAndDefenceJobDetails(models.Model):
    police_defence_id = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Police Defence JobDetails"
