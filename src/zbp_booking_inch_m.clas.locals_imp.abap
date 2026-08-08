CLASS lhc__booking DEFINITION INHERITING FROM cl_abap_behavior_handler.

  PRIVATE SECTION.

    METHODS earlynumbering_cba_Suppl FOR NUMBERING
      IMPORTING entities FOR CREATE _Booking\_Suppl.

ENDCLASS.

CLASS lhc__booking IMPLEMENTATION.

  METHOD earlynumbering_cba_Suppl.
  ENDMETHOD.

ENDCLASS.

*"* use this source file for the definition and implementation of
*"* local helper classes, interface definitions and type
*"* declarations

