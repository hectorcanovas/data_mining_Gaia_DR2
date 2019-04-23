# Codes excluded from my own Classes/Modules but needed for the main codes
import os, glob, getpass, sys, warnings
import itertools
import numpy as np
import matplotlib.pyplot as plt
from astropy           import units as u
from astropy           import wcs
from astropy.table     import Table, join, vstack, hstack, Column, MaskedColumn, unique
from astropy.io        import fits
from astropy.modeling  import models, fitting
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord
from astropy.nddata import Cutout2D
from photutils import CircularAperture, CircularAnnulus, SkyCircularAperture, aperture_photometry, SkyCircularAnnulus


user = getpass.getuser()
sys.path.append('/Users/' + user + '/Dropbox/my_python_packages')
# sys.path.append('/Users/' + user + '/Dropbox/Public/clustering_oph/')
from gaia.photometry import Photometry as phot
from gaia.Basic_Plotters import Basic_Plotters as Basic_Plotters

vizier   = Vizier(columns=["*", "+_r"]) # Nearest Object is the first one of the table

class sample_initial:
    """
    Extra methods used inside "Sample_Initial/ directory"
    """
    def __init__(self):
        pass

    def __repr__(self):
        """Return developer-friendly string representation."""
        return f'Class with dedicated methods to construct the Initial Sample'


    def query_ids_0(inp_id, catalog = "II/246", radius = 1.0 * u.arcsecond, verbose = False):
    # ""
    # NOTEBOOK: "01_read_opf_cats" [/sample_initial/]
    # "Level-0 code to perform individual VizieR searches"
    # ""
        if verbose:
            print('Querying Vizier, ID: ',inp_id)

        viz_0  = vizier.query_object(inp_id,catalog=catalog, radius = radius)
        if len(viz_0) == 0:
            out_tb           = None
        else:
            out_tb           = viz_0[0]
            out_tb['dummy']  = 'N'
            out_tb['inp_id'] = inp_id
        return out_tb


    def query_ids_1(inp_ids, catalog = "II/246", radius = 1.0 * u.arcsecond, verbose = True):
    # ""
    # NOTEBOOK: "01_read_opf_cats" [/sample_initial/]
    # "Level-1 code to perform multiple VizieR searches"
    # ""
        # 1) Construct Dummy Row ===========
        Vizier.ROW_LIMIT  = 1
        cat_0             = Vizier.get_catalogs(catalog)
        dummy_tb          = cat_0[0]
        dummy_tb['_r']    = 0
        dummy_tb['dummy'] = 'Y'
        Vizier.ROW_LIMIT  = -1    

        # 2) Construct Seed Table ==========
        viz_tb = dummy_tb.copy()

        # 3) Add rows to Seed Table ========
        for inp in inp_ids:
            result = sample_initial.query_ids_0(inp,catalog=catalog, radius = radius, verbose = verbose)
            viz_tb = vstack([viz_tb, Table(result)])

        viz_tb       = viz_tb[viz_tb['dummy'] != 'Y']
        viz_tb['_r'] = viz_tb['_r'].to(u.arcsecond)
        viz_tb['_r'].format = '3.2f'
        viz_tb.sort('inp_id')

        return viz_tb


    def query_coords(inp_coords, catalog = "II/246", verbose = False, radius = 1.0*u.arcsecond):
    # ""
    # NOTEBOOK: "01_read_opf_cats" [/sample_initial/]
    # ""
        out_0  = vizier.query_region(inp_coords[0],catalog = catalog, radius = radius)
        out_0  = out_0[0] # Get First table
        out_00 = Table([[0] for inp in out_0.colnames], names = out_0.colnames)

        out_0['inp_id'] = 0
        inp_ids         = iter(range(1,len(inp_coords)))

        for inp in inp_ids:
            if verbose:
                print('Querying Vizier, ID: ',inp)

            result = vizier.query_region(inp_coords[inp],catalog = catalog, radius = radius)
            if len(result) > 0:
                out = result[0]
            else:
                out = out_00

            out['inp_id'] = inp
            row           = out[0]
            out_0.add_row(row)

        out_0['dist']        = out_0['_r'].to(u.arcsecond)
        out_0['dist'].format = '3.2f'
        out_0.remove_column('_r')
        return out_0


    def check_2mass(inp_cat, inp_cat_2mass):
    # ""
    # NOTEBOOK: "01_read_opf_cats" [/sample_initial/]
    # ""
        print(f'Input Targets in 2MASS Catalogue: {len(inp_cat):10.0f}')
        print(f'Missing 2MASS targets: {len(inp_cat) - len(inp_cat_2mass):21.0f}')

        print()


    def read_cats(inp_cat, inp_cat_2mass, verbose = True,
                  cols = ['RAJ2000', 'DEJ2000','_2MASS', 'Jmag', 'e_Jmag', 'Hmag', 'e_Hmag', 'Kmag', 'e_Kmag', 'Qflg','Rflg', 'Bflg', 'Cflg', 'Xflg', 'Aflg']):
    # ""
    # NOTEBOOK: "02_create_Sample_Ini" [/sample_initial/]
    # ""
        inp_cat       = Table.read(inp_cat)
        inp_cat_2mass = Table.read(inp_cat_2mass)
        inp_cat_2mass = inp_cat_2mass[cols]
        inp_cat_2mass.convert_bytestring_to_unicode()

        if verbose:
            sample_initial.check_2mass(inp_cat, inp_cat_2mass)		

        return inp_cat,inp_cat_2mass
        






        
class sample_comp:
    """
    Extra methods used inside "sample_comp/ directory"
    """

    def __init__(self):
        pass

    def __repr__(self):
        """Return developer-friendly string representation."""
        return f'Class with dedicated methods to compare the outputs from DBSCAN, OPTICS, HDBSCAN'

    def read_cluster(inp_path, label, cols = None):
    # ""
    # NOTEBOOK: "01_plot_all_hists" [/sample_comp/]
    # ""
        out = Table.read(inp_path, format = 'votable')
        if cols:
            out  = out[cols]
        out.label = label
        return out
        
        
    def read_fits(inp_path):
    # ""
    # NOTEBOOK: "02_make_common, 04_astrometry_extinction" [/sample_comp/]
    # ""
        hdu  = fits.open(inp_path)
        out  = {'data':hdu[0].data, 'header':hdu[0].header, 'wcs':wcs.WCS(hdu[0].header), 'hdu':hdu[0]}
        hdu.close()
        return out
        
        
        
    def get_hist(hists_dict, hist_label = 'hist_1', hist_index = 0):
    # ""
    # NOTEBOOK: "04_astrometry_extinction" [/sample_comp/]
    # ""
        histogram = hists_dict[hist_label]
        return [histogram['bin_c'][hist_index], histogram['bin_h'][hist_index]]

    def gauss_2_fit(hist_x, hist_y, gauss_1 = (1,0,0.1), gauss_2 = (1,0,0.1), show_plot = True, fit_LevMar = False, verbose = True, vline = None):
    # ""
    # NOTEBOOK: "04_astrometry_extinction" [/sample_comp/]
    # ""
        # Pad input to facilitate the fitting ============
        step   = hist_x[1] - hist_x[0]
        trim   = 30
        for i in range(trim):
            hist_x = np.pad(hist_x, (1,1), 'constant', constant_values=(hist_x[0] - step, hist_x[-1] + step))
            hist_y = np.pad(hist_y, (1,1), 'constant', constant_values=(0, 0))


        # Prepare fit ====================================
        if fit_LevMar == False: fitter = fitting.SLSQPLSQFitter()
        if fit_LevMar == True:  fitter = fitting.LevMarLSQFitter()

        # Construct individual Gaussians (first guess)====
        gaus_1 = models.Gaussian1D(gauss_1[0], gauss_1[1],  gauss_1[2])
        gaus_2 = models.Gaussian1D(gauss_2[0], gauss_2[1],  gauss_2[2])

        # Perform fit & extract models ===================
        gg_fit = fitter(gaus_1 + gaus_2, hist_x, hist_y)
        errors = np.sqrt(np.diag(fitter.fit_info['param_cov'])) # 1 Sigma Error

        gg_fit.amplitude_0_err = errors[0]
        gg_fit.mean_0_err      = errors[1]
        gg_fit.stddev_0_err    = errors[2]
        gg_fit.amplitude_1_err = errors[3]
        gg_fit.mean_1_err      = errors[4]
        gg_fit.stddev_1_err    = errors[5]

        # Construct individual Gaussians (model)==========
        fit_1  = models.Gaussian1D(gg_fit.amplitude_0, gg_fit.mean_0, gg_fit.stddev_0)
        fit_2  = models.Gaussian1D(gg_fit.amplitude_1, gg_fit.mean_1, gg_fit.stddev_1)

        if show_plot:
            hist_x  = hist_x[trim:-trim]
            xi      = np.min(hist_x)
            xf      = np.max(hist_x)
            n_samps = 100
            xrange  = np.arange(xi, xf, np.abs(xi - xf)/n_samps)        

            linewidth = 3
            plt.plot(xrange, gg_fit(xrange), color = 'black',  label = '',  linestyle = '-', linewidth = linewidth)
            plt.plot(xrange, fit_1(xrange),  color = 'black',  label = '',  linestyle = '--', linewidth = linewidth)
            plt.plot(xrange, fit_2(xrange),  color = 'black',  label = '',  linestyle = ':', linewidth = linewidth)

            if vline: plt.vlines(x=vline, ymin=0, ymax=100)

        if verbose:
            sample_comp.model_info(gg_fit)

        return gg_fit


    def model_info(inp_model):
    # ""
    # NOTEBOOK: "04_astrometry_extinction" [/sample_comp/]
    # ""
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Amplitude 1:', inp_model.amplitude_0.value, '+/-', inp_model.amplitude_0_err))
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Mean 1:',      inp_model.mean_0.value,      '+/-', inp_model.mean_0_err))
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Std 1:',       inp_model.stddev_0.value,    '+/-', inp_model.stddev_0_err))
        print()
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Amplitude 2:', inp_model.amplitude_1.value, '+/-', inp_model.amplitude_1_err))
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Mean 2:',      inp_model.mean_1.value,      '+/-', inp_model.mean_1_err))
        print('{:15s}{:5.1f}{:>5s}{:5.1f}'.format('Std 2:',       inp_model.stddev_1.value,    '+/-', inp_model.stddev_1_err))
        

    def plot_stl_07(xlabel = r'$G - G_\mathrm{R}$ [mag]', ylabel = r'$M_\mathrm{G}$ [mag]', fontsize = 18, xlim = [16,0], ylim = [-0.1,2.7]):
    # ""
    # NOTEBOOK: "07_create_CMD" [/sample_comp/]
    # ""
        plt.xlabel(xlabel, fontsize = fontsize)
        plt.ylabel(ylabel, fontsize = fontsize)
        plt.xticks(fontsize = fontsize)
        plt.yticks(fontsize = fontsize)
        plt.xlim(xlim)
        plt.ylim(ylim)


    def plot_1_hist_07(gaia_inp_cat, axis_obj, inp_col = 'phot_g_mean_mag_err', ftsize = 18):
    # ""
    # NOTEBOOK: "07_create_CMD" [/sample_comp/]
    # ""
        Bplotter = Basic_Plotters(gaia_inp_cat)

        hist_1 = Bplotter.plot_hist(inp_col=inp_col, ftsize=ftsize, fig=False)
        hist_x = hist_1['bin_c']
        hist_y = hist_1['bin_h']

        mean_1 = gaia_inp_cat[inp_col].mean()
        maxi_1 = hist_x[np.argmax(hist_y)]

        axis_obj.axvline(x=maxi_1, color = 'k')
        axis_obj.axvline(x=mean_1, color = 'k', linestyle='--')
        
        
    def read_tb_07(inp_tb):
    # ""
    # NOTEBOOK: "07_create_CMD" [/sample_comp/]
    # ""
        out       = Table.read(inp_tb)
        out       = out[out['Mass'].mask == False]
        out.label = inp_tb[inp_tb.rfind('/')+1:inp_tb.rfind('_Table'):]
        return out


    def read_wise_fits_09(path_wise, table_wise, file_index, band = 'w4'):
    # ""
    # NOTEBOOK: "09_make_WISE_ALL_maps" [/sample_comp/]
    # ""
        coords     = [table_wise['wise_ra'][file_index], table_wise['wise_dec'][file_index]]
        fits_files = glob.glob(path_wise + '*' + coords[0] + '*' + coords[1] + '*fits')
        fits_file  = [inp for inp in fits_files if band in inp][0]

        hdu  = fits.open(fits_file)
        out  = {'data':hdu[0].data, 'header':hdu[0].header, 'wcs':wcs.WCS(hdu[0].header), 'hdu':hdu[0], 'coords':coords}
        hdu.close()
        return out


    def zoom_wise_fits_09(read_wise_fits_out, zoom_size = 5 * u.arcmin):
    # ""
    # NOTEBOOK: "09_make_WISE_ALL_maps" [/sample_comp/]
    # ""
        zoom_c  = SkyCoord(ra = read_wise_fits_out['coords'][0], dec = read_wise_fits_out['coords'][1], unit = u.deg, frame = 'icrs')
        zoom    = Cutout2D(read_wise_fits_out['data'], zoom_c, zoom_size, wcs=read_wise_fits_out['wcs'])
        header  = read_wise_fits_out['hdu'].header
        header.update(zoom.wcs.to_header()) # Update input header
        wcs_o   = wcs.WCS(header)      
        out     = {'data':zoom.data, 'header':header, 'wcs':wcs_o, 'coords': read_wise_fits_out['coords'], 'coords_sky':zoom_c}
        return out


    def wise_multiphot_09(table_wise, path_wise, band = 'w1', zoom_size = 2.5* u.arcmin, rad_ap = 12 * u.arcsec, rad_sky_i = 20 * u.arcsec,
    rad_sky_o = 25 * u.arcsec, cmap = 'viridis', ftsize = 14, filename = 'dummy.pdf', figsize   = [30,60], nrows = 13, ncols = 7, hspace = None,
    wspace = None):
    # ""
    # NOTEBOOK: "09_make_WISE_ALL_maps" [/sample_comp/]
    # ""
        sn_band = []
        s_ids   = []
        fig     = plt.figure(figsize=figsize)
        plt.subplots_adjust(hspace = hspace, wspace = wspace)

        for index in range(len(table_wise)):
            inp_img   = sample_comp.read_wise_fits_09(path_wise=path_wise, table_wise=table_wise, band=band, file_index=index)
            inp_img_z = sample_comp.zoom_wise_fits_09(inp_img, zoom_size = zoom_size)
            test_phot = sample_comp.ap_phot(inp_img=inp_img_z, rad_ap = rad_ap, rad_sky_i = rad_sky_i, rad_sky_o = rad_sky_o, show_plot=False)

            sn_out = test_phot['phot_tab']['SN'][0]
            s_id   = table_wise['source_id'][index]
            sn_band.append(sn_out)
            s_ids.append(s_id)

            ax  = plt.subplot(nrows,ncols,1+index)
            img = ax.imshow(inp_img_z['data'], cmap=cmap, interpolation='none', origin='lower')
            test_phot['phot_ap_px'].plot()
            test_phot['phot_sky_px'].plot(color = 'red')

            plt.axis('off')
            ax.text(0.1, 0.9, s_id, fontsize=ftsize, transform=ax.transAxes, bbox={'facecolor':'white', 'alpha':1.0, 'pad':7})

        plt.show()
        fig.savefig(filename, bbox_inches = 'tight', overwrite = True)

        return Table([s_ids, sn_band], names = ['source_id', 'SN'])


    def plot_seds_10(photometry_tb, pdfname = 'seds.pdf', markersize = 10, fontsize = 24, panel_ax = 5, xlim=[10**-1, 10**2], ylim=[10**-16, 10**-10]):
        fig      = plt.figure(figsize=(40,60))

        master_cat = phot()
        master_cat.load_catalogue(photometry_tb)
        for i in range(len(master_cat.cat)):
            plt.subplot(8,5,i+1)
            plt.subplots_adjust(wspace = 0.01, hspace = 0.1)

            tit = '#' + np.str(master_cat.cat['source_id'][i])

            h_axis = [True, True]
            if i % 5 == 0:    h_axis = [True, False]
            if i == panel_ax: h_axis = [False, False]

            master_cat.make_sed_table(index = i)
            master_cat.plot_sed(show_tit = tit, show_plot=False,
                                 hide_xaxis=h_axis[0], hide_yaxis=h_axis[1], xlim=xlim, ylim=ylim, fontsize = fontsize, markersize = markersize)

        plt.show()

        fig.savefig(pdfname, bbox_inches='tight', overwrite = True)


    def get_photmask_stats(phot_px_mask, inp_img):
        inp_mask     = phot_px_mask.to_mask(method = 'center')
        inp_mask_dat = inp_mask[0].multiply(inp_img)

        mask         = inp_mask[0].data # Binary mask
        mask_data    = inp_mask_dat[mask > 0]
        return {'mean':mask_data.mean(), 'std':mask_data.std(), 'max':mask_data.max()}


    def ap_phot(inp_img, rad_ap, rad_sky_i, rad_sky_o, show_plot = True):
        # Define Aperture Pars ===========
        ap       = SkyCircularAperture(inp_img['coords_sky'], r=rad_ap)  # Roughly WISE4 PSF
        sky      = SkyCircularAnnulus( inp_img['coords_sky'], r_in=rad_sky_i, r_out=rad_sky_o)
        ap_px    = ap.to_pixel( wcs=inp_img['wcs'])
        sky_px   = sky.to_pixel(wcs=inp_img['wcs'])


        # Perform Photometry =============
        phot_dat         = aperture_photometry(inp_img['data'], ap,  wcs=inp_img['wcs'])
        phot_sky         = aperture_photometry(inp_img['data'], sky, wcs=inp_img['wcs'])
        bkg_mean         = phot_sky['aperture_sum'] / sky_px.area()
        phot_dat['Phot'] = phot_dat['aperture_sum'] - (bkg_mean * ap_px.area())


        # Compute S/N ====================
        sky_stats = sample_comp.get_photmask_stats(sky_px, inp_img=inp_img['data'])
        ap__stats = sample_comp.get_photmask_stats(ap_px,  inp_img=inp_img['data'])
        phot_dat['SN'] = (ap__stats['max'] - sky_stats['mean'])/sky_stats['std']

        for col in ['aperture_sum', 'Phot', 'SN']:
            phot_dat[col].format = '10.2f'

        if show_plot:
            fig = plt.figure(figsize=[7,7])
            ax  = plt.subplot(111)

            img         = ax.imshow(inp_img['data'], origin = 'lower', cmap = 'viridis')
            ap_px.plot()
            sky_px.plot(color = 'red')
            plt.show()

        return {'phot_tab':phot_dat, 'phot_ap_px':ap_px, 'phot_sky_px':sky_px}        