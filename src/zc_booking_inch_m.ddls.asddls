@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection view for Booking'
define view entity ZC_BOOKING_INCH_M as projection on ZI_BOOING_INCH_M
{
    key TravelId,
    key BookingId,
    BookingDate,
    CustomerId,
    CarrierId,
    ConnectionId,
    FlightDate,
    FlightPrice,
    CurrencyCode,
    BookingStatus,
    LastChangedAt,
    /* Associations */
    _BookSt,
    _Carrier,
    _Connection,
    _Customer,
    _Suppl: redirected to composition child ZC_BOOKING_SUPPL_M,
    _Travel: redirected to parent ZC_TRAVEL_ROOT_INCH
}
