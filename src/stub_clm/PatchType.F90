module PatchType

  !-----------------------------------------------------------------------
  ! !DESCRIPTION:
  ! Patch data type allocation
  ! --------------------------------------------------------
  ! patch types can have values of
  ! --------------------------------------------------------
  !   0  => not vegetated
  !   1  => needleleaf evergreen temperate tree
  !   2  => needleleaf evergreen boreal tree
  !   3  => needleleaf deciduous boreal tree
  !   4  => broadleaf evergreen tropical tree
  !   5  => broadleaf evergreen temperate tree
  !   6  => broadleaf deciduous tropical tree
  !   7  => broadleaf deciduous temperate tree
  !   8  => broadleaf deciduous boreal tree
  !   9  => broadleaf evergreen shrub
  !   10 => broadleaf deciduous temperate shrub
  !   11 => broadleaf deciduous boreal shrub
  !   12 => c3 arctic grass
  !   13 => c3 non-arctic grass
  !   14 => c4 grass
  !   15 => c3_crop
  !   16 => c3_irrigated
  !   17 => corn
  !   18 => irrigated corn
  !   19 => spring temperate cereal
  !   20 => irrigated spring temperate cereal
  !   21 => winter temperate cereal
  !   22 => irrigated winter temperate cereal
  !   23 => soybean
  !   24 => irrigated soybean
  ! --------------------------------------------------------
  !
  use shr_kind_mod   , only : r8 => shr_kind_r8
  use shr_infnan_mod , only : nan => shr_infnan_nan, assignment(=)
  use clm_varcon     , only : ispval, spval
  use decompMod      , only : bounds_type
  !
  ! !PUBLIC TYPES:
  implicit none
  save
  private
  !
  type, public :: patch_type
     ! g/l/c/p hierarchy, local g/l/c/p cells only
     integer , pointer :: column   (:) => null()! index into column level quantities
     real(r8), pointer :: wtcol    (:) => null()! weight (relative to column)
     integer , pointer :: landunit (:) => null()! index into landunit level quantities
     real(r8), pointer :: wtlunit  (:) => null()! weight (relative to landunit)
     integer , pointer :: gridcell (:)=> null() ! index into gridcell level quantities
     real(r8), pointer :: wtgcell  (:) => null()! weight (relative to gridcell)

     ! topological mapping functionality
     integer , pointer :: itype    (:) => null()! patch vegetation
     integer , pointer :: mxy      (:) => null()! m index for laixy(i,j,m),etc. (undefined for special landunits)
     logical , pointer :: active   (:) => null()! true=>do computations on this patch

   contains

     procedure, public :: Init
     procedure, public :: Clean

  end type patch_type
  type(patch_type), public, target :: pft  ! patch type data structure !***TODO*** - change the data instance to patch from pft
  !------------------------------------------------------------------------

contains

  !------------------------------------------------------------------------
  subroutine Init(this, bounds)
    !
    ! !ARGUMENTS:
    class(patch_type)   :: this
    type(bounds_type), intent(in) :: bounds
    !
    ! LOCAL VARAIBLES:
    integer :: begp, endp
    !------------------------------------------------------------------------
    begp=bounds%begp; endp=bounds%endp
    ! The following is set in InitGridCells
    allocate(this%gridcell (begp:endp)); this%gridcell (:) = ispval
    allocate(this%wtgcell  (begp:endp)); this%wtgcell  (:) = spval
    allocate(this%landunit (begp:endp)); this%landunit (:) = ispval
    allocate(this%wtlunit  (begp:endp)); this%wtlunit  (:) = spval
    allocate(this%column   (begp:endp)); this%column   (:) = ispval
    allocate(this%wtcol    (begp:endp)); this%wtcol    (:) = spval
    allocate(this%itype    (begp:endp)); this%itype    (:) = ispval
    allocate(this%mxy      (begp:endp)); this%mxy      (:) = ispval
    allocate(this%active   (begp:endp)); this%active   (:) = .false.

  end subroutine Init

  !------------------------------------------------------------------------
  subroutine Clean(this)
    !
    ! !ARGUMENTS:
    class(patch_type) :: this
    !------------------------------------------------------------------------

    deallocate(this%gridcell)
    deallocate(this%wtgcell )
    deallocate(this%landunit)
    deallocate(this%wtlunit )
    deallocate(this%column  )
    deallocate(this%wtcol   )
    deallocate(this%itype   )
    deallocate(this%mxy     )
    deallocate(this%active  )

  end subroutine Clean

end module PatchType
