
#define     NULL						((void*)0)


enum {
	False,
	True
}bool;


#define 	UDS_VALID_FRAME        (1)
#define		UDS_INVALID_FRAME      (0)

typedef enum 
{
	UDS_No_Security_Level,         
 	UDS_Security_Level_Zero,       
 	UDS_Security_Level_One        

}UDS_SecurityAccess_t;


#define		DIAGNOSTIC_SESSION_CONTROL_SID  	     (0x10)
#define		ECU_RESET_SID                          	 (0x11)
#define		SECUIRITY_ACCESS_SID                     (0x27)
#define     READ_DATA_BY_IDENTIFIER_SID              (0x22)
#define     CLEAR_DIAGNOSTIC_INFORMATION_SID         (0x14)
#define     READ_DTC_INFORMATION_SID 		         (0x19)




#define   GENERAL_REJECT_NRC                    (0x10)


typedef enum 
{
	GeneralReject= 0x10,
	serviceNotSupported=0x11,
	subFunctionNotSupported=0x12,
	incorrectMessageLengthOrInvalidFormat=0x13,
	conditonsNotCorrect=0x22,
	requestOutOfRange=0x31,
	securityAccessDenied=0x33,
	invalidKey=0x35,
	subFunctionNotSupportedInActiveSession=0x7E,
	serviceNotSupportedInActiveSession=0x7F,
	temperatureTooHigh=0x86,
	temperatureTooLow=0x87,
	voltageTooHigh=0x92,
	voltageTooLow=0x93

}UDS_negativeResponseCode_t;

//DTC Status Byte
typedef struct 
{
	
	u8  testFailed 					       : 1 ; /* DTC failed at the time of the request (0x01) */
	u8  testFailedThisOperationCycle       : 1 ; /* DTC failed on the current operation cycle (0x02) */
	u8  pendingDTC 					       : 1 ; /* DTC failed on the current or previous operation cycle */
	u8	confirmedDTC 				       : 1 ; /* DTC is confirmed at the time of the request (0x08) */
	u8	testNotCompletedSinceLastClear 	   : 1 ; /* DTC test not completed since the last code clear (0x10) */
	u8	testFailedSinceLastClear		   : 1 ; /* DTC test failed at least once since last code clear (0x20) */
	u8	testNotCompletedThisOperationCycle : 1 ; /* DTC test not completed this operation cycle (0x40) */
	u8	warningIndicatorRequested		   : 1 ; /* Server is requesting warningIndicator to be active(0x80) */

}DTC_Statu_Byte_t;

DTC_Statu_Byte_t     DTC_Statu_Byte;


typedef enum
{
	Default_Session=0x01,
	Programming_Session,
	Extended_Diagnostic_Session,
	UDS_SAFETY_SYSTEM_DIAGNOSTIC

}UDS_Session_t;


typedef enum
{
	UDS_positveResponse,
	UDS_negativeResponse

}UDS_Response_t;


typedef struct
{
u8   SID  ; /* Service ID           -0x00 --> 0x3E- */
u8   SBF  ; /* SUB Function ID           -optional- */
u16  DID  ; /* Data ID                   -optional- */
u8 * Data ; /* Data Pointer has no limit -optional- */

}UDS_Frame_t;


typedef struct
{
	UDS_Frame_t        			Service_Frame;
	UDS_Session_t               Session;
	UDS_SecurityAccess_t        SecuirtyLevel;

}UDS_Services_t;


typedef enum 
{
	ECU_softReset,
	ECU_warmReset,
	ECU_hardReset,

}ECU_Reset_t;


extern UDS_Services_t ECU_Reset =
{
		{
				ECU_RESET_SID, /* SID */
				0x03, /* SUB Function -Soft Reset- */
				0,    /* Data ID */
				NULL  /* Data    */
		},
		Default_Session, 				      /* Session       */
		UDS_No_Security_Level                 /* SecuirtyLevel */

};



extern UDS_Services_t Diagnostic_Session_Control =
{
		{
				0x10, /* SID */
				0x03, /* SUB Function -Soft Reset- */
				0,    /* Data ID */
				NULL  /* Data    */
		},
		Default_Session, /* Session       */
		UDS_No_Security_Level                 /* SecuirtyLevel */

};


u8 UDS_Session_Control( UDS_Session_t Session );

//
//typedef struct
//{
//
//}UDS_Sessions;



/**********************************[APIs]***********************************/

