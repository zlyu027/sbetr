#!/usr/bin/env python2
#in app_namePara create two files
#CMakeLists.txt

def Make1layer(sfarm_dir, app_name):
    print "create file "+sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/CMakeLists.txt"
    fcmake=open(sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/CMakeLists.txt","w")
    fcmake.write("set("+app_name.upper()+"1LAYER_SOURCES\n")
    fcmake.write("  "+app_name+"BGCIndexType.F90\n")
    fcmake.write("  "+app_name+"BGCType.F90\n")
    fcmake.write(")\n")
    fcmake.write("\n")
    fcmake.write("include_directories(${CMAKE_BINARY_DIR}/src/betr/betr_util)\n")
    fcmake.write("include_directories(${CMAKE_BINARY_DIR}/src/betr/betr_math)\n")
    fcmake.write("include_directories(${CMAKE_BINARY_DIR}/src/Applications/soil-farm/bgcfarm_util)\n")
    fcmake.write("include_directories(${CMAKE_BINARY_DIR}/src/Applications/soil-farm/"+app_name+"/"+app_name+"Para)\n")
    fcmake.write("include(add_betr_library)\n")
    fcmake.write("add_betr_library("+app_name+"1layer ${"+app_name.upper()+"1LAYER_SOURCES})\n")
    fcmake.write("\n")
    fcmake.write("set(BETR_LIBRARIES "+app_name+"1layer;${BETR_LIBRARIES} PARENT_SCOPE)\n")
    fcmake.write("set(BETR_LIBRARIES "+app_name+"1layer;${BETR_LIBRARIES})\n")
    fcmake.write("\n")
#X#add_subdirectory(tests)
    fcmake.write("if (NOT CMAKE_INSTALL_PREFIX STREQUAL "+'"'+"INSTALL_DISABLED"+'"'+")\n")
    fcmake.write("   install(TARGETS "+app_name+"1layer DESTINATION lib)\n")
    fcmake.write("   file(GLOB HEADERS *.h)\n")
    fcmake.write("   install(FILES ${HEADERS} DESTINATION include/soil-farm/"+app_name+"/"+app_name+"1layer)\n")
    fcmake.write("endif()\n")
    fcmake.close()

    print "create file "+sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/"+app_name+"BGCIndexType.F90"
    ff90=open(sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/"+app_name+"BGCIndexType.F90","w")
    ff90.write("module "+app_name+"BGCIndexType\n")
    ff90.write("  use bshr_kind_mod  , only : r8 => shr_kind_r8\n")
    ff90.write("  use betr_varcon    , only : var_flux_type, var_state_type\n")
    ff90.write("implicit none\n")
    ff90.write("private\n")
    ff90.write("  character(len=*), private, parameter :: mod_filename = &\n")
    ff90.write("       __FILE__\n")
    ff90.write("\n")
    ff90.write("integer, parameter :: loc_name_len=64\n")
    ff90.write("\n")
    ff90.write("  type, public :: "+app_name+"_bgc_index_type\n")
    ff90.write("    integer           :: nelms\n")
    ff90.write("    integer           :: nstvars          !number of equations for the state variabile vector\n")
    ff90.write("    integer           :: nreactions\n")
    ff90.write("  contains\n")
    ff90.write("    procedure, public  :: Init\n")
    ff90.write("  end type "+app_name+"_bgc_index_type\n")
    ff90.write("contains\n")
    ff90.write(" !-------------------------------------------------------------------------------\n")
    ff90.write("  subroutine Init(this)\n")
    ff90.write("  !\n")
    ff90.write("  ! DESCRIPTION:\n")
    ff90.write("  ! Initialize "+app_name+"_bgc_index_type\n")
    ff90.write("  ! !USES:\n")
    ff90.write("  implicit none\n")
    ff90.write("  ! !ARGUMENTS:\n")
    ff90.write("  class("+app_name+"_bgc_index_type), intent(inout) :: this\n")
    ff90.write("  \n")
    ff90.write("  this%nelms=1\n")
    ff90.write("  this%nstvars=1\n")
    ff90.write("  this%nreactions=1\n")
    ff90.write("  end subroutine Init\n")
    ff90.write("\n")
    ff90.write("end module "+app_name+"BGCIndexType\n")
    ff90.write("\n")
    ff90.close()
    print "create file "+sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/"+app_name+"BGCType.F90"
    ff90=open(sfarm_dir+'/'+app_name+'/'+app_name+'1layer'+"/"+app_name+"BGCType.F90","w")
    ff90.write("module "+app_name+"BGCType\n")
    ff90.write("#include "+'"'+"bshr_assert.h"+'"\n')
    ff90.write("  !\n")
    ff90.write("  ! !DESCRIPTION:\n")
    ff90.write("\n")
    ff90.write("  ! !USES:\n")
    ff90.write("  use bshr_kind_mod             , only : r8 => shr_kind_r8\n")
    ff90.write("  use bshr_log_mod              , only : errMsg => shr_log_errMsg\n")
    ff90.write("  use betr_varcon               , only : spval => bspval\n")
    ff90.write("  use betr_ctrl                 , only : spinup_state => betr_spinup_state\n")
    ff90.write("  use gbetrType                 , only : gbetr_type\n")
    ff90.write("  use "+app_name+"ParaType             , only : "+app_name+"_para_type\n")
    ff90.write("  use BetrStatusType            , only : betr_status_type\n")
    ff90.write("  use "+app_name+"BGCIndexType            , only : "+app_name+"_bgc_index_type\n")
    ff90.write("  implicit none\n")
    ff90.write("  private\n")
    ff90.write("  character(len=*), private, parameter :: mod_filename = &\n")
    ff90.write("       __FILE__\n")
    ff90.write("\n")
    ff90.write("  type, public :: "+app_name+"_bgc_type\n")
    ff90.write("  type("+app_name+"_bgc_index_type),     private :: "+app_name+"_index\n")
    ff90.write("\n")
    ff90.write("    !declare parameters below\n")
    ff90.write("\n")
    ff90.write("  contains\n")
    ff90.write("    procedure, public  :: init          => init_"+app_name+"\n")
    ff90.write("    procedure, public  :: runbgc        => runbgc_"+app_name+"\n")
    ff90.write("    procedure, public  :: init_cold     => init_cold_"+app_name+"\n")
    ff90.write("  end type "+app_name+"_bgc_type\n")
    ff90.write("contains\n")
    ff90.write("\n")
    ff90.write("  !-------------------------------------------------------------------------------\n")
    ff90.write("\n")
    ff90.write("  subroutine init_"+app_name+"(this, batch_mode,  bstatus)\n")
    ff90.write("  use betr_varcon         , only : betr_maxpatch_pft\n")
    ff90.write("  implicit none\n")
    ff90.write("  class("+app_name+"_bgc_type) , intent(inout) :: this\n")
    ff90.write("  logical, optional, intent(in) :: batch_mode\n")
    ff90.write("  type(betr_status_type)      , intent(out) :: bstatus\n")
    ff90.write("  !local variables\n")
    ff90.write("  character(len=256) :: msg\n")
    ff90.write("\n")
    ff90.write("  end subroutine init_"+app_name+"\n")
    ff90.write("  !-------------------------------------------------------------------------------\n")

    ff90.write("  subroutine runbgc_"+app_name+"(this,  is_surflit, dtime, bgc_forc, nstates, ystates0, ystatesf, bstatus)\n")
    ff90.write("\n")
    ff90.write("  !DESCRIPTION\n")
    ff90.write("  !do bgc model integration for one step\n")
    ff90.write("  use JarBgcForcType        , only : JarBGC_forc_type\n")
    ff90.write("  use BetrStatusType        , only : betr_status_type\n")
    ff90.write("  use tracer_varcon         , only : catomw, natomw, patomw\n")
    ff90.write("  implicit none\n")
    ff90.write("  class("+app_name+"_bgc_type)  , intent(inout) :: this\n")
    ff90.write("  logical                    , intent(in)    :: is_surflit\n")
    ff90.write("  real(r8)                   , intent(in)    :: dtime\n")
    ff90.write("  type(JarBGC_forc_type)     , intent(in)    :: bgc_forc\n")
    ff90.write("  integer                    , intent(in)    :: nstates\n")
    ff90.write("  real(r8)                   , intent(out)   :: ystates0(nstates)\n")
    ff90.write("  real(r8)                   , intent(out)   :: ystatesf(nstates)\n")
    ff90.write("  type(betr_status_type)     , intent(out)   :: bstatus\n")
    ff90.write("\n")
    ff90.write("  !local variables\n")
    ff90.write("  real(r8)               :: time = 0._r8\n")
    ff90.write("  character(len=*),parameter :: subname = 'runbgc_"+app_name+"'\n")
    ff90.write("\n")

    ff90.write("  end subroutine runbgc_"+app_name+"\n")
    ff90.write("  !-------------------------------------------------------------------------------\n")
    ff90.write("  subroutine init_cold_"+app_name+"(this, nstvars, ystates)\n")
    ff90.write("  !\n")
    ff90.write("  !DESCRPTION\n")
    ff90.write("  !do a cold state initialization for batch mode simulation\n")
    ff90.write("  implicit none\n")
    ff90.write("  class("+app_name+"_bgc_type)     , intent(inout) :: this\n")
    ff90.write("  integer                   , intent(in)    :: nstvars\n")
    ff90.write("  real(r8)                  , intent(inout) :: ystates(nstvars)\n")
    ff90.write("\n")
    ff90.write("  !Initialize necessary state variables below\n")
    ff90.write("  end subroutine init_cold_"+app_name+"\n")
    ff90.write("  end module "+app_name+"BGCType\n")
    ff90.close()
