/****************************************
 * NVM.c
 *
 *  Created on: Mar 13, 2022
 *      Author: Ahmed-Nasr
 ******************************************/

#include "STD_TYPES.h"
#include "BIT_MATH.h"

#include "NvM.h"

#include "FPEC_interface.h"

u8 NvM_WriteBlock(NvM_BlockIdType * copy_u8DataId , u16 * copy_u16ptrData )
{
	/*EREASE PAGE*/
	FPEC_voidFlashPageErase( (u8)((NvM_BASE_ADDRESS - 0x0800000)/1024) );

	/*FPEC WRITE*/
	 FPEC_voidFlashWrite( copy_u8DataId->BlockAddress , copy_u16ptrData , copy_u8DataId->BlockSize);

	 return 1 ;
}
u8 NvM_ReadBlock(NvM_BlockIdType * copy_u8DataId  , u32 * copy_u16ptrData )
{

	*copy_u16ptrData = *( (u32*)(copy_u8DataId->BlockAddress) );
	return 1 ;
}
