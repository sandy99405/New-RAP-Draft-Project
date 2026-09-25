sap.ui.define([
    "sap/m/MessageBox",
    "sap/m/MessageToast",
    "sap/ui/core/Fragment"
], function(MessageBox, MessageToast, Fragment){
       'use strict';

       return{
           onSendToAgent: function(oEvent){

                debugger;
                var oView = this.getView();

                var oTextArea = oView.byId("agentInput") || Fragment.byId(oView.getId(), "agentInput");

                if(!oTextArea){
                    MessageToast.show("Input data missing");
                    return;
                }

                var sUserPrompt = oTextArea.getValue();
                if(!sUserPrompt.trim()){
                    MessageToast.show("Please Enter a prompt");
                    return;
                }

                fetch("http://localhost:5000/api/agent", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt: sUserPrompt })
                })
                .then(function(oResponse){
                    debugger;
                     if(!oResponse.ok){
                        throw new Error();
                     }
                     return oResponse.json();
                })
                .then(function(oData){
                    debugger;
                    if(oData && oData.response){
                        MessageBox.information(oData.response, {
                            duration: 5000,
                            width: "25em",
                            title: "AI Agent Response",
                        styleClass: "sapUiSizeCompact"
                        });
                    }else{
                        debugger;
                        MessageToast.show("Recieved empty response from Agent and Inchara Loves Sandilya",
                            { duration: 10000,
                                width: "30em"
                            });
                    }
                })
                .catch(function(oError){
                    console.error(oError);
                    MessageToast.show("You Came here because Inchara Loves Sandilya");
                });
                // .then(res => res.json())
                // .then(data => {
                //     MessageToast.show(data.response);
                // })
                // .catch(err => {
                //     console.error("Python Server unreachable:", err);
                //     MessageToast.show("Error connecting to Python Agent server.");
                // });
           }
       };
});




