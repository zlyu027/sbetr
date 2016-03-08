# This function adds a pfunit test executable for BeTR.
function(add_betr_unit_test exe)
  configure_file(${CMAKE_BINARY_DIR}/include/driver.F90 driver.F90 COPYONLY)
  add_executable(${exe} ${ARGN} driver.F90)
  target_link_libraries(${exe} pfunit;${BETR_LIBRARIES})
  include_directories(${CMAKE_BINARY_DIR}/mod)
  include_directories(${CMAKE_BINARY_DIR}/src/shr)
  include_directories(${CMAKE_BINARY_DIR}/src/betr/betr_math)
  set_target_properties(${exe} PROPERTIES LINKER_LANGUAGE Fortran)
  set_target_properties(${exe} PROPERTIES COMPILE_FLAGS "-DCMAKE_CURRENT_SOURCE_DIR=\\\"${CMAKE_CURRENT_SOURCE_DIR}\\\"")
  add_test(${exe} ${exe})
  set_tests_properties(${exe} PROPERTIES WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
endfunction()
