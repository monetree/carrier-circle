
from django.db import models
from scrap import models as scrap_models
"""
-------------------------------------------------
        @@ MODELS FOR ALL INDIA GOVT JobDetails @@    ||
-------------------------------------------------
"""

class UpscJobDetails(models.Model):
    upsc_details_id= models.AutoField(primary_key=True)
    upsc            = models.OneToOneField(scrap_models.UpscJobs,on_delete=models.CASCADE,related_name='upsc_details')
    more_info       = models.TextField()
    join_id         = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Upsc JobDetails"

class SscJobDetails(models.Model):
    ssc_details_id= models.AutoField(primary_key=True)
    ssc            = models.OneToOneField(scrap_models.SscJobs,on_delete=models.CASCADE,related_name='ssc_details')
    more_info      = models.TextField()
    join_id        = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Ssc JobDetails"

class OtherAllIndiaJobDetails(models.Model):
    other_all_india_details_id= models.AutoField(primary_key=True)
    # other_all_india            = models.OneToOneField(scrap_models.OtherAllIndiaJobs,on_delete=models.CASCADE,related_name='other_all_india_details')
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
    odisha_details_id= models.AutoField(primary_key=True)
    # odisha            = models.OneToOneField(scrap_models.OdishaGovtJobs,on_delete=models.CASCADE,related_name='odisha_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Odisha Govt JobDetails"

class AndamanNicoborGovtJobDetails(models.Model):
    andaman_details_id= models.AutoField(primary_key=True)
    # andaman            = models.OneToOneField(scrap_models.AndamanNicoborGovtJobs,on_delete=models.CASCADE,related_name='andaman_details')
    more_info          = models.TextField()
    join_id            = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Govt JobDetails"

class AndhraPradeshGovtJobDetails(models.Model):
    andhra_details_id = models.AutoField(primary_key=True)
    # andhra            = models.OneToOneField(scrap_models.AndhraPradeshGovtJobs,on_delete=models.CASCADE,related_name='andhra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Govt JobDetails"

class ArunachalPradeshGovernmentJobDetails(models.Model):
    arunachal_details_id     = models.AutoField(primary_key=True)
    # arunachal            = models.OneToOneField(scrap_models.ArunachalPradeshGovernmentjobs,on_delete=models.CASCADE,related_name='arunachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Govt JobDetails"

class AssamGovtJobDetails(models.Model):
    assam_details_id         = models.AutoField(primary_key=True)
    # assam            = models.OneToOneField(scrap_models.AssamGovtJobs,on_delete=models.CASCADE,related_name='assam_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Govt JobDetails"

class BiharGovtJobDetails(models.Model):
    bihar_details_id         = models.AutoField(primary_key=True)
    # bihar            = models.OneToOneField(scrap_models.BiharGovtJobs,on_delete=models.CASCADE,related_name='bihar_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Govt JobDetails"

class ChandigarhGovtJobDetails(models.Model):
    chandigarh_details_id    = models.AutoField(primary_key=True)
    # chandigarh            = models.OneToOneField(scrap_models.ChandigarhGovtJobs,on_delete=models.CASCADE,related_name='chandigarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Govt JobDetails"

class ChhattisgarhGovtJobDetails(models.Model):
    chhattisgarh_details_id  = models.AutoField(primary_key=True)
    # chhattisgarh            = models.OneToOneField(scrap_models.ChhattisgarhGovtJobs,on_delete=models.CASCADE,related_name='chhattisgarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Govt JobDetails"

class DadraNagarHaveliGovtJobDetails(models.Model):
    dadra_nagar_haveli_details_id= models.AutoField(primary_key=True)
    # dadra_nagar_haveli            = models.OneToOneField(scrap_models.DadraNagarHaveliGovtJobs,on_delete=models.CASCADE,related_name='dadra_nagar_haveli_details')
    more_info             = models.TextField()
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Govt JobDetails"

class DamanDiuGovtJobDetails(models.Model):
    daman_diu_details_id     = models.AutoField(primary_key=True)
    # daman_diu            = models.OneToOneField(scrap_models.DamanDiuGovtJobs,on_delete=models.CASCADE,related_name='daman_diu_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Govt JobDetails"

class DelhiGovtJobDetails(models.Model):
    delhi_details_id        = models.AutoField(primary_key=True)
    # delhi            = models.OneToOneField(scrap_models.DelhiGovtJobs,on_delete=models.CASCADE,related_name='delhi_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Govt JobDetails"

class GoaGovernmentJobDetails(models.Model):
    goa_details_id           = models.AutoField(primary_key=True)
    # goa            = models.OneToOneField(scrap_models.GoaGovernmentjobs,on_delete=models.CASCADE,related_name='goa_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Govt JobDetails"

class GujuratGovtJobDetails(models.Model):
    gujurat_details_id       = models.AutoField(primary_key=True)
    # gujurat            = models.OneToOneField(scrap_models.GujuratGovtJobs,on_delete=models.CASCADE,related_name='gujurat_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Govt JobDetails"

class HaryanaGovtJobDetails(models.Model):
    haryana_details_id         = models.AutoField(primary_key=True)
    # haryana            = models.OneToOneField(scrap_models.HaryanaGovtJobs,on_delete=models.CASCADE,related_name='haryana_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Govt JobDetails"

class HimachalPradeshGovtJobDetails(models.Model):
    himachal_details_id      = models.AutoField(primary_key=True)
    # himachal            = models.OneToOneField(scrap_models.HimachalPradeshGovtJobs,on_delete=models.CASCADE,related_name='himachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Govt JobDetails"

class JammuKashmirGovtJobDetails(models.Model):
    jammu_kashmir_details_id = models.AutoField(primary_key=True)
    # jammu_kashmir            = models.OneToOneField(scrap_models.JammuKashmirGovtJobs,on_delete=models.CASCADE,related_name='jammu_kashmir_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Govt JobDetails"

class JharkhandGovtJobDetails(models.Model):
    jharkhand_details_id     = models.AutoField(primary_key=True)
    # jharkhand            = models.OneToOneField(scrap_models.JharkhandGovtJobs,on_delete=models.CASCADE,related_name='jharkhand_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Govt JobDetails"

class KarnatakaGovtJobDetails(models.Model):
    karnataka_details_id     = models.AutoField(primary_key=True)
    # karnataka            = models.OneToOneField(scrap_models.KarnatakaGovtJobs,on_delete=models.CASCADE,related_name='karnataka_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Govt JobDetails"

class KeralaGovtJobDetails(models.Model):
    kerala_details_id        = models.AutoField(primary_key=True)
    # kerala            = models.OneToOneField(scrap_models.KeralaGovtJobs,on_delete=models.CASCADE,related_name='kerala_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Govt JobDetails"

class LakshadweepGovernmentJobDetails(models.Model):
    lakshadweep_details_id   = models.AutoField(primary_key=True)
    # lakshadweep            = models.OneToOneField(scrap_models.LakshadweepGovernmentjobs,on_delete=models.CASCADE,related_name='lakshadweep_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Govt JobDetails"

class MadhyaPradeshGovtJobDetails(models.Model):
    madhya_pradesh_details_id= models.AutoField(primary_key=True)
    # madhya_pradesh            = models.OneToOneField(scrap_models.MadhyaPradeshGovtJobs,on_delete=models.CASCADE,related_name='madhya_pradesh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Govt JobDetails"

class MaharashtraGovtJobDetails(models.Model):
    maharashtra_details_id   = models.AutoField(primary_key=True)
    # maharashtra            = models.OneToOneField(scrap_models.MaharashtraGovtJobs,on_delete=models.CASCADE,related_name='maharashtra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Govt JobDetails"

class ManipurGovtJobDetails(models.Model):
    manipur_details_id       = models.AutoField(primary_key=True)
    # manipur            = models.OneToOneField(scrap_models.ManipurGovtJobs,on_delete=models.CASCADE,related_name='manipur_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Govt JobDetails"

class MeghalayaGovtJobDetails(models.Model):
    meghalaya_details_id  = models.AutoField(primary_key=True)
    # meghalaya            = models.OneToOneField(scrap_models.MeghalayaGovtJobs,on_delete=models.CASCADE,related_name='meghalaya_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Govt JobDetails"

class MizoramGovtJobDetails(models.Model):
    mizoram_details_id       = models.AutoField(primary_key=True)
    # mizoram            = models.OneToOneField(scrap_models.MizoramGovtJobs,on_delete=models.CASCADE,related_name='mizoram_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Govt JobDetails"

class NagalandGovtJobDetails(models.Model):
    nagaland_details_id      = models.AutoField(primary_key=True)
    # nagaland            = models.OneToOneField(scrap_models.NagalandGovtJobs,on_delete=models.CASCADE,related_name='nagaland_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Govt JobDetails"

class PuduchheryGovtJobDetails(models.Model):
    puduchhery_details_id    = models.AutoField(primary_key=True)
    # puduchhery            = models.OneToOneField(scrap_models.PuduchheryGovtJobs,on_delete=models.CASCADE,related_name='puduchhery_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Govt JobDetails"

class PunjabGovernmentJobDetails(models.Model):
    punjab_details_id        = models.AutoField(primary_key=True)
    # punjab            = models.OneToOneField(scrap_models.PunjabGovernmentjobs,on_delete=models.CASCADE,related_name='punjab_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Govt JobDetails"

class RajasthanGovtJobDetails(models.Model):
    rajasthan_details_id     = models.AutoField(primary_key=True)
    # rajasthan            = models.OneToOneField(scrap_models.RajasthanGovtJobs,on_delete=models.CASCADE,related_name='rajasthan_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Govt JobDetails"

class SikkimGovtJobDetails(models.Model):
    sikkim_details_id         = models.AutoField(primary_key=True)
    # sikkim            = models.OneToOneField(scrap_models.SikkimGovtJobs,on_delete=models.CASCADE,related_name='sikkim_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Govt JobDetails"

class TamilGovtJobDetails(models.Model):
    tamil_details_id         = models.AutoField(primary_key=True)
    # tamil            = models.OneToOneField(scrap_models.TamilGovtJobs,on_delete=models.CASCADE,related_name='tamil_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Govt JobDetails"

class TelanganaGovtJobDetails(models.Model):
    telangana_details_id     = models.AutoField(primary_key=True)
    # telangana            = models.OneToOneField(scrap_models.TelanganaGovtJobs,on_delete=models.CASCADE,related_name='telangana_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Govt JobDetails"

class TripuraGovtJobDetails(models.Model):
    tripura_details_id       = models.AutoField(primary_key=True)
    # tripura            = models.OneToOneField(scrap_models.TripuraGovtJobs,on_delete=models.CASCADE,related_name='tripura_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Govt JobDetails"

class UttarakhandGovtJobDetails(models.Model):
    uttarakhand_details_id   = models.AutoField(primary_key=True)
    # uttarakhand            = models.OneToOneField(scrap_models.UttarakhandGovtJobs,on_delete=models.CASCADE,related_name='uttarakhand_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Govt JobDetails"

class UttarPradeshGovtJobDetails(models.Model):
    uttar_pradesh_details_id = models.AutoField(primary_key=True)
    # uttar_pradesh            = models.OneToOneField(scrap_models.UttarPradeshGovtJobs,on_delete=models.CASCADE,related_name='uttar_pradesh_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Govt JobDetails"

class WestBengalGovtJobDetails(models.Model):
    west_bengal_details_id   = models.AutoField(primary_key=True)
    # west_bengal            = models.OneToOneField(scrap_models.WestBengalGovtJobs,on_delete=models.CASCADE,related_name='west_bengal_details')
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
    bankJobDetails_details_id      = models.AutoField(primary_key=True)
    # bankjobs            = models.OneToOneField(scrap_models.AllBankJobs,on_delete=models.CASCADE,related_name='bankjobs_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "All Bank JobDetails"


class OtherFinancialJobDetails(models.Model):
    financialJobDetails_details_id = models.AutoField(primary_key=True)
    # financialjobs            = models.OneToOneField(scrap_models.OtherFinancialJobs,on_delete=models.CASCADE,related_name='other_financialjobs_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Other Financial JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE TEACHING JobDetails @@    ||
-------------------------------------------------
"""


class AllIndiaTeachingJobDetails(models.Model):
    all_india_details_id     = models.AutoField(primary_key=True)
    # all_india            = models.OneToOneField(scrap_models.AllIndiaTeachingJobs,on_delete=models.CASCADE,related_name='all_india_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Teaching JobDetails"

class AndamanNicoborTeachingJobDetails(models.Model):
    andaman_details_id       = models.AutoField(primary_key=True)
    # andaman            = models.OneToOneField(scrap_models.AndamanNicoborTeachingJobs,on_delete=models.CASCADE,related_name='andaman_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Teaching JobDetails"

class AndhraPradeshTeachingJobDetails(models.Model):
    andhra_details_id        = models.AutoField(primary_key=True)
    # andhra            = models.OneToOneField(scrap_models.AndhraPradeshTeachingJobs,on_delete=models.CASCADE,related_name='andhra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Teaching JobDetails"

class ArunachalPradeshTeachingJobDetails(models.Model):
    arunachal_details_id     = models.AutoField(primary_key=True)
    # arunachal            = models.OneToOneField(scrap_models.ArunachalPradeshTeachingJobs,on_delete=models.CASCADE,related_name='arunachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Teaching JobDetails"

class AssamTeachingJobDetails(models.Model):
    assam_details_id         = models.AutoField(primary_key=True)
    # assam            = models.OneToOneField(scrap_models.AssamTeachingJobs,on_delete=models.CASCADE,related_name='assam_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Teaching JobDetails"

class BiharTeachingJobDetails(models.Model):
    bihar_details_id         = models.AutoField(primary_key=True)
    # bihar            = models.OneToOneField(scrap_models.BiharTeachingJobs,on_delete=models.CASCADE,related_name='bihar_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Teaching JobDetails"

class ChandigarhTeachingJobDetails(models.Model):
    chandigarh_details_id    = models.AutoField(primary_key=True)
    # chandigarh            = models.OneToOneField(scrap_models.ChandigarhTeachingJobs,on_delete=models.CASCADE,related_name='chandigarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Teaching JobDetails"

class ChhattisgarhTeachingJobDetails(models.Model):
    chhattisgarh_details_id  = models.AutoField(primary_key=True)
    # chhattisgarh            = models.OneToOneField(scrap_models.ChhattisgarhTeachingJobs,on_delete=models.CASCADE,related_name='chhattisgarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Teaching JobDetails"

class DadraNagarHaveliTeachingJobDetails(models.Model):
    dadra_nagar_haveli_details_id= models.AutoField(primary_key=True)
    # dadra_nagar_haveli            = models.OneToOneField(scrap_models.DadraNagarHaveliTeachingJobs,on_delete=models.CASCADE,related_name='dadra_nagar_haveli_details')
    more_info             = models.TextField()
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Teaching JobDetails"

class DamanDiuTeachingJobDetails(models.Model):
    DamanDiuTeachingJobDetails      = models.AutoField(primary_key=True)
    # daman_diu            = models.OneToOneField(scrap_models.DamanDiuTeachingJobs,on_delete=models.CASCADE,related_name='daman_diu_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Teaching JobDetails"

class DelhiTeachingJobDetails(models.Model):
    delhi_details_id        = models.AutoField(primary_key=True)
    # delhi            = models.OneToOneField(scrap_models.DelhiTeachingJobs,on_delete=models.CASCADE,related_name='delhi_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Teaching JobDetails"

class GoaTeachingJobDetails(models.Model):
    goa_details_id           = models.AutoField(primary_key=True)
    # goa            = models.OneToOneField(scrap_models.GoaTeachingJobs,on_delete=models.CASCADE,related_name='goa_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Teaching JobDetails"

class GujuratTeachingJobDetails(models.Model):
    gujurat_details_id       = models.AutoField(primary_key=True)
    # gujurat            = models.OneToOneField(scrap_models.GujuratTeachingJobs,on_delete=models.CASCADE,related_name='gujurat_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Teaching JobDetails"

class HaryanaTeachingJobDetails(models.Model):
    haryana_details_id         = models.AutoField(primary_key=True)
    # haryana            = models.OneToOneField(scrap_models.HaryanaTeachingJobs,on_delete=models.CASCADE,related_name='haryana_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Teaching JobDetails"

class HimachalPradeshTeachingJobDetails(models.Model):
    himachal_details_id      = models.AutoField(primary_key=True)
    # himachal            = models.OneToOneField(scrap_models.HimachalPradeshTeachingJobs,on_delete=models.CASCADE,related_name='himachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Teaching JobDetails"

class JammuKashmirTeachingJobDetails(models.Model):
    jammu_kashmir_details_id = models.AutoField(primary_key=True)
    # jammu_kashmir            = models.OneToOneField(scrap_models.JammuKashmirTeachingJobs,on_delete=models.CASCADE,related_name='jammu_kashmir_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Teaching JobDetails"

class JharkhandTeachingJobDetails(models.Model):
    jharkhand_details_id     = models.AutoField(primary_key=True)
    # jharkhand            = models.OneToOneField(scrap_models.JharkhandTeachingJobs,on_delete=models.CASCADE,related_name='jharkhand_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Teaching JobDetails"

class KarnatakaTeachingJobDetails(models.Model):
    karnataka_details_id     = models.AutoField(primary_key=True)
    # karnataka            = models.OneToOneField(scrap_models.KarnatakaTeachingJobs,on_delete=models.CASCADE,related_name='karnataka_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Teaching JobDetails"

class KeralaTeachingJobDetails(models.Model):
    kerala_details_id        = models.AutoField(primary_key=True)
    # kerala            = models.OneToOneField(scrap_models.KeralaTeachingJobs,on_delete=models.CASCADE,related_name='kerala_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Teaching JobDetails"

class LakshadweepTeachingJobDetails(models.Model):
    lakshadweep_details_id   = models.AutoField(primary_key=True)
    # lakshadweep            = models.OneToOneField(scrap_models.LakshadweepTeachingJobs,on_delete=models.CASCADE,related_name='lakshadweep_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Teaching JobDetails"

class MadhyaPradeshTeachingJobDetails(models.Model):
    madhya_pradesh_details_id= models.AutoField(primary_key=True)
    # madhya_pradesh            = models.OneToOneField(scrap_models.MadhyaPradeshTeachingJobs,on_delete=models.CASCADE,related_name='madhya_pradesh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Teaching JobDetails"

class MaharashtraTeachingJobDetails(models.Model):
    maharashtra_details_id   = models.AutoField(primary_key=True)
    # maharashtra            = models.OneToOneField(scrap_models.MaharashtraTeachingJobs,on_delete=models.CASCADE,related_name='maharashtra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Teaching JobDetails"

class ManipurTeachingJobDetails(models.Model):
    manipur_details_id       = models.AutoField(primary_key=True)
    # manipur            = models.OneToOneField(scrap_models.ManipurTeachingJobs,on_delete=models.CASCADE,related_name='manipur_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Teaching JobDetails"

class MeghalayaTeachingJobDetails(models.Model):
    meghalaya_details_id  = models.AutoField(primary_key=True)
    # meghalaya            = models.OneToOneField(scrap_models.MeghalayaTeachingJobs,on_delete=models.CASCADE,related_name='meghalaya_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Teaching JobDetails"

class MizoramTeachingJobDetails(models.Model):
    mizoram_details_id       = models.AutoField(primary_key=True)
    # mizoram            = models.OneToOneField(scrap_models.MizoramTeachingJobs,on_delete=models.CASCADE,related_name='mizoram_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Teaching JobDetails"

class NagalandTeachingJobDetails(models.Model):
    nagaland_details_id      = models.AutoField(primary_key=True)
    # nagaland            = models.OneToOneField(scrap_models.NagalandTeachingJobs,on_delete=models.CASCADE,related_name='nagaland_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Teaching JobDetails"

class OdishaTeachingJobDetails(models.Model):
    odisha_details_id    = models.AutoField(primary_key=True)
    # odisha            = models.OneToOneField(scrap_models.OdishaTeachingJobs,on_delete=models.CASCADE,related_name='odisha_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Teaching JobDetails"

class PuduchheryTeachingJobDetails(models.Model):
    punjab_details_id        = models.AutoField(primary_key=True)
    # puduchhery            = models.OneToOneField(scrap_models.PuduchheryTeachingJobs,on_delete=models.CASCADE,related_name='puduchhery_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching JobDetails"

class PunjabTeachingJobDetails(models.Model):
    punjab_details_id        = models.AutoField(primary_key=True)
    # punjab            = models.OneToOneField(scrap_models.PunjabTeachingJobs,on_delete=models.CASCADE,related_name='punjab_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching JobDetails"

class RajasthanTeachingJobDetails(models.Model):
    rajasthan_details_id     = models.AutoField(primary_key=True)
    # rajasthan            = models.OneToOneField(scrap_models.RajasthanTeachingJobs,on_delete=models.CASCADE,related_name='rajasthan_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Teaching JobDetails"

class SikkimTeachingJobDetails(models.Model):
    sikkim_details_id         = models.AutoField(primary_key=True)
    # sikkim            = models.OneToOneField(scrap_models.SikkimTeachingJobs,on_delete=models.CASCADE,related_name='sikkim_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Teaching JobDetails"

class TamilNaduTeachingJobDetails(models.Model):
    tamil_details_id         = models.AutoField(primary_key=True)
    # tamil            = models.OneToOneField(scrap_models.TamilNaduTeachingJobs,on_delete=models.CASCADE,related_name='tamil_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Teaching JobDetails"

class TelanganaTeachingJobDetails(models.Model):
    telangana_details_id     = models.AutoField(primary_key=True)
    # telangana            = models.OneToOneField(scrap_models.TelanganaTeachingJobs,on_delete=models.CASCADE,related_name='telangana_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Teaching JobDetails"

class TripuraTeachingJobDetails(models.Model):
    tripura_details_id       = models.AutoField(primary_key=True)
    # tripura            = models.OneToOneField(scrap_models.TripuraTeachingJobs,on_delete=models.CASCADE,related_name='tripura_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Teaching JobDetails"

class UttarakhandTeachingJobDetails(models.Model):
    uttarakhand_details_id   = models.AutoField(primary_key=True)
    # uttarakhand            = models.OneToOneField(scrap_models.UttarakhandTeachingJobs,on_delete=models.CASCADE,related_name='uttarakhand_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Teaching JobDetails"

class UttarPradeshTeachingJobDetails(models.Model):
    uttar_pradesh_details_id = models.AutoField(primary_key=True)
    # uttar_pradesh            = models.OneToOneField(scrap_models.UttarPradeshTeachingJobs,on_delete=models.CASCADE,related_name='uttar_pradesh_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Teaching JobDetails"

class WestBengalTeachingJobDetails(models.Model):
    west_bengal_details_id   = models.AutoField(primary_key=True)
    # west_bengal            = models.OneToOneField(scrap_models.WestBengalTeachingJobs,on_delete=models.CASCADE,related_name='west_bengal_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Teaching JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE ENGINEERING JobDetails @@    ||
-------------------------------------------------
"""


class AllIndiaEnggJobDetails(models.Model):
    all_india_details_id     = models.AutoField(primary_key=True)
    # all_india            = models.OneToOneField(scrap_models.AllIndiaEnggJobs,on_delete=models.CASCADE,related_name='all_india_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Engg JobDetails"


class AllIndiaFellowEnggJobDetails(models.Model):
    all_india_details_id     = models.AutoField(primary_key=True)
    # all_india_fellow            = models.OneToOneField(scrap_models.AllIndiaFellowEnggJobs,on_delete=models.CASCADE,related_name='all_india_fellow_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AllIndia Fellow Engg JobDetails"

class AndamanNicoborEnggJobDetails(models.Model):
    andaman_details_id       = models.AutoField(primary_key=True)
    # andaman            = models.OneToOneField(scrap_models.AndamanNicoborEnggJobs,on_delete=models.CASCADE,related_name='andaman_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Engg JobDetails"

class AndhraPradeshEnggJobDetails(models.Model):
    andhra_details_id        = models.AutoField(primary_key=True)
    # andhra            = models.OneToOneField(scrap_models.AndhraPradeshEnggJobs,on_delete=models.CASCADE,related_name='andhra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Engg JobDetails"

class ArunachalPradeshEnggJobDetails(models.Model):
    arunachal_details_id     = models.AutoField(primary_key=True)
    # arunachal            = models.OneToOneField(scrap_models.ArunachalPradeshEnggJobs,on_delete=models.CASCADE,related_name='arunachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Engg JobDetails"

class AssamEnggJobDetails(models.Model):
    assam_details_id         = models.AutoField(primary_key=True)
    # assam            = models.OneToOneField(scrap_models.AssamEnggJobs,on_delete=models.CASCADE,related_name='assam_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Engg JobDetails"

class BiharEnggJobDetails(models.Model):
    bihar_details_id         = models.AutoField(primary_key=True)
    # bihar            = models.OneToOneField(scrap_models.BiharEnggJobs,on_delete=models.CASCADE,related_name='bihar_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Engg JobDetails"

class ChandigarhEnggJobDetails(models.Model):
    chandigarh_details_id    = models.AutoField(primary_key=True)
    # chandigarh            = models.OneToOneField(scrap_models.ChandigarhEnggJobs,on_delete=models.CASCADE,related_name='chandigarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Engg JobDetails"

class ChhattisgarhEnggJobDetails(models.Model):
    chhattisgarh_details_id  = models.AutoField(primary_key=True)
    # chhattisgarh            = models.OneToOneField(scrap_models.ChhattisgarhEnggJobs,on_delete=models.CASCADE,related_name='chhattisgarh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Engg JobDetails"

class DadraNagarHaveliEnggJobDetails(models.Model):
    dadra_nagar_haveli_details_id= models.AutoField(primary_key=True)
    # dadra_nagar_haveli            = models.OneToOneField(scrap_models.DadraNagarHaveliEnggJobs,on_delete=models.CASCADE,related_name='dadra_nagar_haveli_details')
    more_info             = models.TextField()
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Engg JobDetails"

class DamanDiuEnggJobDetails(models.Model):
    DamanDiuEnggJobDetails      = models.AutoField(primary_key=True)
    # daman_diu            = models.OneToOneField(scrap_models.DamanDiuEnggJobs,on_delete=models.CASCADE,related_name='daman_diu_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DamanDiu Engg JobDetails"

class DelhiEnggJobDetails(models.Model):
    delhi_details_id        = models.AutoField(primary_key=True)
    # delhi            = models.OneToOneField(scrap_models.DelhiEnggJobs,on_delete=models.CASCADE,related_name='delhi_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Delhi Engg JobDetails"

class GoaEnggJobDetails(models.Model):
    goa_details_id           = models.AutoField(primary_key=True)
    # goa            = models.OneToOneField(scrap_models.GoaEnggJobs,on_delete=models.CASCADE,related_name='goa_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Engg JobDetails"

class GujuratEnggJobDetails(models.Model):
    gujurat_details_id       = models.AutoField(primary_key=True)
    # gujurat            = models.OneToOneField(scrap_models.GujuratEnggJobs,on_delete=models.CASCADE,related_name='gujurat_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Gujurat Engg JobDetails"

class HaryanaEnggJobDetails(models.Model):
    haryana_details_id         = models.AutoField(primary_key=True)
    # haryana            = models.OneToOneField(scrap_models.HaryanaEnggJobs,on_delete=models.CASCADE,related_name='haryana_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Haryana Engg JobDetails"

class HimachalPradeshEnggJobDetails(models.Model):
    himachal_details_id      = models.AutoField(primary_key=True)
    # himachal            = models.OneToOneField(scrap_models.HimachalPradeshEnggJobs,on_delete=models.CASCADE,related_name='himachal_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "HimachalPradesh Engg JobDetails"

class JammuKashmirEnggJobDetails(models.Model):
    jammu_kashmir_details_id = models.AutoField(primary_key=True)
    # jammu_kashmir            = models.OneToOneField(scrap_models.JammuKashmirEnggJobs,on_delete=models.CASCADE,related_name='jammu_kashmir_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "JammuKashmir Engg JobDetails"

class JharkhandEnggJobDetails(models.Model):
    jharkhand_details_id     = models.AutoField(primary_key=True)
    # jharkhand            = models.OneToOneField(scrap_models.JharkhandEnggJobs,on_delete=models.CASCADE,related_name='jharkhand_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Jharkhand Engg JobDetails"

class KarnatakaEnggJobDetails(models.Model):
    karnataka_details_id     = models.AutoField(primary_key=True)
    # karnataka            = models.OneToOneField(scrap_models.KarnatakaEnggJobs,on_delete=models.CASCADE,related_name='karnataka_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "karnataka Engg JobDetails"

class KeralaEnggJobDetails(models.Model):
    kerala_details_id        = models.AutoField(primary_key=True)
    # kerala            = models.OneToOneField(scrap_models.KeralaEnggJobs,on_delete=models.CASCADE,related_name='kerala_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Kerala Engg JobDetails"

class LakshadweepEnggJobDetails(models.Model):
    lakshadweep_details_id   = models.AutoField(primary_key=True)
    # lakshadweep            = models.OneToOneField(scrap_models.LakshadweepEnggJobs,on_delete=models.CASCADE,related_name='lakshadweep_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Lakshadweep Engg JobDetails"

class MadhyaPradeshEnggJobDetails(models.Model):
    madhya_pradesh_details_id= models.AutoField(primary_key=True)
    # madhya_pradesh            = models.OneToOneField(scrap_models.MadhyaPradeshEnggJobs,on_delete=models.CASCADE,related_name='madhya_pradesh_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "MadhyaPradesh Engg JobDetails"

class MaharashtraEnggJobDetails(models.Model):
    maharashtra_details_id   = models.AutoField(primary_key=True)
    # maharashtra            = models.OneToOneField(scrap_models.MaharashtraEnggJobs,on_delete=models.CASCADE,related_name='maharashtra_details')
    more_info         = models.TextField()
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Maharashtra Engg JobDetails"

class ManipurEnggJobDetails(models.Model):
    manipur_details_id       = models.AutoField(primary_key=True)
    # manipur            = models.OneToOneField(scrap_models.ManipurEnggJobs,on_delete=models.CASCADE,related_name='manipur_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Engg JobDetails"

class MeghalayaEnggJobDetails(models.Model):
    meghalaya_details_id  = models.AutoField(primary_key=True)
    # meghalaya            = models.OneToOneField(scrap_models.MeghalayaEnggJobs,on_delete=models.CASCADE,related_name='meghalaya_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Engg JobDetails"

class MizoramEnggJobDetails(models.Model):
    mizoram_details_id       = models.AutoField(primary_key=True)
    # mizoram            = models.OneToOneField(scrap_models.MizoramEnggJobs,on_delete=models.CASCADE,related_name='mizoram_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Engg JobDetails"

class NagalandEnggJobDetails(models.Model):
    nagaland_details_id      = models.AutoField(primary_key=True)
    # nagaland            = models.OneToOneField(scrap_models.NagalandEnggJobs,on_delete=models.CASCADE,related_name='nagaland_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Engg JobDetails"

class OdishaEnggJobDetails(models.Model):
    odisha_details_id    = models.AutoField(primary_key=True)
    # odisha            = models.OneToOneField(scrap_models.OdishaEnggJobs,on_delete=models.CASCADE,related_name='odisha_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Engg JobDetails"

class PuduchheryEnggJobDetails(models.Model):
    puduchhery_details_id        = models.AutoField(primary_key=True)
    # puduchhery            = models.OneToOneField(scrap_models.PuduchheryEnggJobs,on_delete=models.CASCADE,related_name='puduchhery_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg JobDetails"

class PunjabEnggJobDetails(models.Model):
    punjab_details_id        = models.AutoField(primary_key=True)
    # punjab            = models.OneToOneField(scrap_models.PunjabEnggJobs,on_delete=models.CASCADE,related_name='punjab_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg JobDetails"

class RajasthanEnggJobDetails(models.Model):
    rajasthan_details_id     = models.AutoField(primary_key=True)
    # rajasthan            = models.OneToOneField(scrap_models.RajasthanEnggJobs,on_delete=models.CASCADE,related_name='rajasthan_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Engg JobDetails"

class SikkimEnggJobDetails(models.Model):
    sikkim_details_id         = models.AutoField(primary_key=True)
    # sikkim            = models.OneToOneField(scrap_models.SikkimEnggJobs,on_delete=models.CASCADE,related_name='sikkim_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Engg JobDetails"

class TamilNaduEnggJobDetails(models.Model):
    tamil_details_id         = models.AutoField(primary_key=True)
    # tamil            = models.OneToOneField(scrap_models.TamilNaduEnggJobs,on_delete=models.CASCADE,related_name='tamil_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Engg JobDetails"

class TelanganaEnggJobDetails(models.Model):
    telangana_details_id     = models.AutoField(primary_key=True)
    # telangana            = models.OneToOneField(scrap_models.TelanganaEnggJobs,on_delete=models.CASCADE,related_name='telangana_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Engg JobDetails"

class TripuraEnggJobDetails(models.Model):
    tripura_details_id       = models.AutoField(primary_key=True)
    # tripura            = models.OneToOneField(scrap_models.TripuraEnggJobs,on_delete=models.CASCADE,related_name='tripura_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Engg JobDetails"

class UttarakhandEnggJobDetails(models.Model):
    uttarakhand_details_id   = models.AutoField(primary_key=True)
    # uttarakhand            = models.OneToOneField(scrap_models.UttarakhandEnggJobs,on_delete=models.CASCADE,related_name='uttarakhand_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Engg JobDetails"

class UttarPradeshEnggJobDetails(models.Model):
    uttar_pradesh_details_id = models.AutoField(primary_key=True)
    # uttar_pradesh            = models.OneToOneField(scrap_models.UttarPradeshEnggJobs,on_delete=models.CASCADE,related_name='uttar_pradesh_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Engg JobDetails"

class WestBengalEnggJobDetails(models.Model):
    west_bengal_details_id   = models.AutoField(primary_key=True)
    # west_bengal            = models.OneToOneField(scrap_models.WestBengalEnggJobs,on_delete=models.CASCADE,related_name='west_bengal_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Engg JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR RAILWAY JobDetails @@    ||
-------------------------------------------------
"""


class RailwayJobDetails(models.Model):
    railway_details_id       = models.AutoField(primary_key=True)
    # railway            = models.OneToOneField(scrap_models.RailwayJob,on_delete=models.CASCADE,related_name='railway_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Railway JobDetails JobDetails"


"""
-------------------------------------------------
        @@ MODELS FOR POLICE AND DEFENCE JobDetails @@    ||
-------------------------------------------------
"""

class StatewisePoliceJobDetails(models.Model):
    statewise_police_details_id= models.AutoField(primary_key=True)
    # statewise_police            = models.OneToOneField(scrap_models.StatewisePoliceJobs,on_delete=models.CASCADE,related_name='statewise_police_details')
    more_info           = models.TextField()
    join_id             = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Statewise Police JobDetails"

class PoliceAndDefenceJobDetails(models.Model):
    police_defence_details_id= models.AutoField(primary_key=True)
    # police_defence            = models.OneToOneField(scrap_models.PoliceAndDefenceJobs,on_delete=models.CASCADE,related_name='police_defence_details')
    more_info         = models.TextField()
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Police Defence JobDetails"
