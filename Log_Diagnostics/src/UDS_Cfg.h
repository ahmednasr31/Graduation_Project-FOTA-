
#ifndef     _UDS_CFG_H_
#define     _UDS_CFG_H_


typedef struct 
{
    u32 S3_Server;      /* Session Timeout (When Timeout Session Transion
                            From non-Default To Default Session)                     */
    u32 P2_Server;     /* The Time Between [Request] And The [First pending Respond] */
    u32 P2_StarServer; /* The Time Between [Each pending Respond] And [The Next one] */

} UDS_Time_t;

/* Time In --Seconds */
UDS_Time_t UDS_Time_Cfg = { 0,0,0 };















#endif