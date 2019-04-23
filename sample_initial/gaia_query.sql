-- Query to Crossmatch (by 2MASS ID) an input table against Gaia DR2 ---------------
select gaia."ra", gaia."dec", gaia."source_id", gaia."parallax", gaia."parallax_error",gaia."parallax_over_error", 
gaia."pmra", gaia."pmra_error", gaia."pmdec", gaia."pmdec_error", gaia."phot_g_mean_mag",gaia."phot_g_mean_flux_over_error", 
gaia."phot_bp_mean_flux_over_error",gaia."phot_bp_mean_mag", gaia."phot_rp_mean_flux_over_error", gaia."phot_rp_mean_mag",
gaia."radial_velocity", gaia."radial_velocity_error", gaia."teff_val", gaia."teff_percentile_lower",gaia."teff_percentile_upper", gaia."a_g_val", gaia."a_g_percentile_lower", gaia."a_g_percentile_upper", gaia."a_g_percentile_upper", gaia."astrometric_excess_noise", gaia."astrometric_excess_noise_sig", gaia."astrometric_chi2_al", gaia."astrometric_n_good_obs_al",gaia."visibility_periods_used", gaia."phot_bp_rp_excess_factor",gaia."bp_rp",sample_ini."jmag",sample_ini."col2mass"

from user_hcanovas.sample_initial_oph as sample_ini

left outer join gaiadr2.tmass_best_neighbour as xmatch
  on sample_ini.col2mass = xmatch.original_ext_source_id
left outer join gaiadr2.gaia_source as gaia
  on xmatch.source_id = gaia.source_id
