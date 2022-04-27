/*
 * main.c
 *
 *  Created on: Mar 13, 2022
 *      Author: Ahmed-Nasr
 */

#include "STD_TYPES.h"
#include "BIT_MATH.h"

#include "NvM.h"
#include "RCC_interface.h"
#include "FPEC_interface.h"


NvM_BlockIdType  Kilometer_Block = { 0x20 , 2 ,NvM_BASE_ADDRESS };

u16 arr[]={0xFAFD,0xFCFB};

void main(void)
{
	u32 Flash_Reading = 0;

	RCC_voidInitSysClock();
	RCC_voidEnableClock(RCC_AHB,4);   /* FPEC   */

	NvM_WriteBlock( &Kilometer_Block , arr);

	NvM_ReadBlock( &Kilometer_Block  , &Flash_Reading );


	while(1)
	{
      asm("NOP");

	}
}
