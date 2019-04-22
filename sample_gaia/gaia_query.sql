SELECT "ra", "dec", "source_id", "parallax", "parallax_error","parallax_over_error", 
"pmra", "pmra_error", "pmdec", "pmdec_error", "phot_g_mean_mag","phot_g_mean_flux_over_error", 
"phot_bp_mean_flux_over_error","phot_bp_mean_mag", "phot_rp_mean_flux_over_error", "phot_rp_mean_mag",
"radial_velocity", "radial_velocity_error", "teff_val", "teff_percentile_lower","teff_percentile_upper", "a_g_val", "a_g_percentile_lower",
"a_g_percentile_upper", "a_g_percentile_upper", "astrometric_excess_noise", "astrometric_excess_noise_sig", "astrometric_chi2_al",
"astrometric_n_good_obs_al","visibility_periods_used", "phot_bp_rp_excess_factor", "bp_rp"


FROM gaiadr2.gaia_source 
WHERE 1=CONTAINS(
  POINT('ICRS',ra,dec),
  CIRCLE('ICRS',247.0,-24.0, 3.5)) 
AND parallax >= 5 AND parallax <= 9
AND parallax/parallax_error >10
