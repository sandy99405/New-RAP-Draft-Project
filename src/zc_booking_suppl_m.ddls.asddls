@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View for Supplements'
@Metadata.allowExtensions: true
define view entity ZC_BOOKING_SUPPL_M
  as projection on ZI_BOOKING_SUPPL_M
{
  key TravelId,
  key BookingId,
  key BookingSupplementId,
      SupplementId,
      Price,
      CurrencyCode,
      LastChangedAt,
      /* Associations */
      _booking : redirected to parent ZC_BOOKING_INCH_M,
      _Supplement,
      _supptext,
      _Travel
}
