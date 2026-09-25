sap.ui.define([
    "sap/m/MessageToast"
], function(MessageToast) {
    'use strict';

    return {
        NewFunction: function(oEvent) {
            MessageToast.show("Custom handler invoked.");
        }
    }
});
