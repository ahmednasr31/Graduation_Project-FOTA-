/*
 * UDS.c
 *
 *  Created on: Mar 13, 2022
 *      Author: Ahmed-Nasr
 */

#include "STD_TYPES.h"

#include "UDS.h"
#include "UDS_Cbf.h"
#include "UDS_Cfg.h"

#include "NvM.h"

/*------------------------ [ Global Variables ] -------------------------------*/

/* Current Session --> Initailly is Default Session */
UDS_Session_t Active_Session = Default_Session ;
/* Current Secuirty Level --> Initailly is ---------  */
UDS_SecurityAccess_t Current_SecuirityLevel = UDS_No_Security_Level ; 

/* Current UDS Service (By Default ... ) */
UDS_Services_t 	Active_UDS_Service  ;



void UDS_PodtBuildInit( void )
{
	asm("NOP");
}
u8 UDS_PodtBuildInit( u8 UDS_configs)
{
	/*Initialize UDS Times */
	asm("NOP");
	return 0 ;

}


/* UDS_mainFunction :
 *
 * Parameters :
 *
 * Return :
 *
 * Description:
 *  Reschedule By OS
 *  -If There Is An UDS Request -> Get The Request + Lock Reception
 *  -Check The Request SID Session
 *  -Check The Request SID Security Access
 *
 *  -
 *
 * */
void UDS_mainFunction(void)
{

}



/**********************************************
 UDS_isValidFrame:
	Parameters:
		UDS_Request [ UDS_Services_t  ]
	Return:
		Local_u8FrameStatus [ u8 ]
					UDS_VALID_FRAME   [1]
					UDS_INVALID_FRAME [0]
	Implementation:
		Check Frame Validation Reande [0x00 -- 0x3E] 
		Return Local_u8FrameStatus
		--should send negative response -- 
		--should check the whole frame
------------almost completed-----------------	
**********************************************/
u8 UDS_isValidFrame(void)
{
	u8 Local_u8FrameStatus=0;

	/* Check SID Validation (Range 0x00 -- 0x3E) */
	if ( (Active_UDS_Service.Service_Frame.SID >= 0x00 )&&(Active_UDS_Service.Service_Frame.SID <= 0x3E) )
		Local_u8FrameStatus = UDS_VALID_FRAME ; 
	else
		Local_u8FrameStatus = UDS_INVALID_FRAME ;

	return Local_u8FrameStatus;	 
}



/*
	u8 UDS_CheckSession();
	u8 UDS_CheckSecurityAccess();
*/


/*
 * Reschedule By OS
 *
 * */
u8 UDS_sendRespond( UDS_Response_t  ResponseToSend  )
{
	if( UDS_negativeResponse  == ResponseToSend )
	{
		//UDS_SendPositveResponse();
	}
	else( UDS_positveResponse == ResponseToSend )
	{
		UDS_SendNigativeResponse();
	}
	return 0;

}

u8 UDS_u8GetRequest( UDS_Services_t UDS_Request )
{	
	UDS_Response_t ResponseToSend; 

	/* Check SID Validation  */
	if ( UDS_isValidFrame(UDS_Request) )

		switch (UDS_Request.Service_Frame.SID)
		{
			case DIAGNOSTIC_SESSION_CONTROL_SID:
				//ResponseToSend = UDS_Session_Control(UDS_Request.Service_Frame.SBF);
				Active_UDS_Service = Diagnostic_Session_Control ;
				break;

			case SECUIRITY_ACCESS_SID:
				break;

			case ECU_RESET_SID :
				break;
			case READ_DATA_BY_IDENTIFIER_SID:
				break;

			case CLEAR_DIAGNOSTIC_INFORMATION_SID :
				break;
			case READ_DTC_INFORMATION_SID :

				break;

			default: break;
		}

	else
	{
		/* SID Not Valid */
	}

	UDS_sendRespond(ResponseToSend);

}

/*

*/
u8 UDS_SendPositveResponse( u32 Request )
{
 

}

u8 UDS_SendNigativeResponse()
{
	u8 * NegativeFrame="7F"+Active_Session.SID;

}

/**********************************************
 UDS_Session_Control:
	Parameters:
			Session [ UDS_Session_t ]
	Return:
			0 [u8]

	Implementation:
		Check security level 
		Assign the session 
		--should send negative response -- 
------------almost completed-----------------	
**********************************************/
u8 UDS_Session_Control( UDS_Session_t Session )
{
	if ( Diagnostic_Session_Control.SecuirtyLevel == Current_SecuirityLevel )
	{
		Active_Session = Session ; 
	}
	else
	{
	/*  UDS_SendNegativeResponse(SECUIRITY_ACCESS_DENID); */
	}
	return 0;
}




/**********************************************
 UDS_ECU_Reset:
	Parameters:
			Reset_Type [ ECU_Reset_t ]
	Return:
			0 [u8]

	Implementation:
		
------------- NOT Completed ------------------	
**********************************************/

u8 UDS_ECU_Reset( ECU_Reset_t  Reset_Type )
{
	if ( Active_Session  )
	{
		if ( Current_SecuirityLevel )
	
	switch (Reset_Type)
	{
	case ECU_softReset:
		/* code */
		break;
	case ECU_warmReset:
		/* code */
		break;
	case ECU_hardReset:
		/* code */
		break;

	default:
		break;
	}

	}
	
}




UDS_Response_t UDS_ReadDTC_Infromation()
{


}
