&sbetr_driver
  simulator_name = 'standalone'
  run_type='sbgc'
  case_id='exp.noadv'
  continue_run=.false.
/

&betr_parameters
  reaction_method = 'summs'
  advection_on = .true.
  diffusion_on = .true.
  reaction_on  = .true.
  ebullition_on= .true.
  input_only   = .false.
  bgc_param_file='/global/home/users/zlyu/temp_sbetr/sbetr/tools/sbgc.ecacnp_pars.06292018.nc'
/

&betr_time
  delta_time=1800.
  stop_n = 200
  hist_freq=30
  stop_option='nyears'
/

&forcing_inparm
  forcing_filename = '/global/scratch/zlyu/e3smcase_tr_20190226_01.clm2.h1.1860-80-2.nc'
  use_rootsoit=.false.
/

&betr_grid
  grid_data_filename = '/global/home/users/zlyu/temp_sbetr/sbetr/input_data/clm_exp_grid.cdl.nc'
/

&regression_test
/
