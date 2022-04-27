
#ifndef   _NvM_H_
#define   _NvM_H_
/**/
/* 58 */
#define   NvM_BASE_ADDRESS            0x0800E800
//#define NvM_PAGES_NUMBER

/* Block Type */

typedef  struct
{
	u8 	BlockID     ;
	u8 	BlockSize   ;
	u32 BlockAddress;
}NvM_BlockIdType;



u8 NvM_WriteBlock(NvM_BlockIdType * copy_u8DataId , u16 * copy_u16ptrData );

u8 NvM_ReadBlock(NvM_BlockIdType * copy_u8DataId  , u32 * copy_u16ptrData );


#endif


