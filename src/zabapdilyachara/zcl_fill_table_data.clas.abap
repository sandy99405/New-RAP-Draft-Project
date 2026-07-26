CLASS zcl_fill_table_data DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
         INTERFACES if_oo_adt_classrun.
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.



CLASS zcl_fill_table_data IMPLEMENTATION.
       method if_oo_adt_classrun~main.
            data lt_entities type table of ZSRT_BILL_ITEM.

            delete from zsrt_bill_item.

            lt_entities = value #(
                 ( client = sy-mandt materialid = '1000' billid = '2000' itemno = '3000' description = 'First Bill' )
                 ( client = sy-mandt materialid = '2000' billid = '2200' itemno = '3329' description = 'Second Bill' )
                 ( client = sy-mandt materialid = '3000' billid = '3000' itemno = '2300' description = 'Third Bill' )
             ).

            insert zsrt_bill_item from table @lt_entities.

            if sy-subrc = 0.
                out->write( 'Completed Successfully !!' ).
            endif.

       endmethod.
ENDCLASS.
