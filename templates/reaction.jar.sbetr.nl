&jar_driver
  jarmodel_name = 'simic'
  phosphorus_stress=.false.
  nitrogen_stress=.true.
  case_id='exp1'
/

&betr_time
  delta_time=1800.
  stop_n = 30
  stop_option='nyears'
/

&forcing_inparm
  forcing_filename = '../regression-tests/input-data/jarmodel_example.halfhour.forcing.nc'
/