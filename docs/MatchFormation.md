# MatchFormation

Team formation about a given match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_sec** | **int** | The absolute second from the tagged video in which the formation finished being used | [optional] 
**id** | **int** |  | [optional] 
**match_period_end** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Period&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;1H&lt;/td&gt;&lt;td&gt;First Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;2H&lt;/td&gt;&lt;td&gt;Second Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E1&lt;/td&gt;&lt;td&gt;First Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E2&lt;/td&gt;&lt;td&gt;Second Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**match_period_start** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Period&lt;/th&gt;&lt;th&gt;Description&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;1H&lt;/td&gt;&lt;td&gt;First Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;2H&lt;/td&gt;&lt;td&gt;Second Half Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E1&lt;/td&gt;&lt;td&gt;First Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;E2&lt;/td&gt;&lt;td&gt;Second Extra Time&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**players** | [**List[PlayersListInner]**](PlayersListInner.md) | List of players in the current formation | [optional] 
**players_on_field** | **int** | The current amount of players present on the field | [optional] 
**scheme** | **str** | &lt;table&gt;&lt;thead&gt;&lt;tr&gt;&lt;th&gt;Scheme&lt;/th&gt;&lt;th&gt;p0&lt;/th&gt;&lt;th&gt;p1&lt;/th&gt;&lt;th&gt;p2&lt;/th&gt;&lt;th&gt;p3&lt;/th&gt;&lt;th&gt;p4&lt;/th&gt;&lt;th&gt;p5&lt;/th&gt;&lt;th&gt;p6&lt;/th&gt;&lt;th&gt;p7&lt;/th&gt;&lt;th&gt;p8&lt;/th&gt;&lt;th&gt;p9&lt;/th&gt;&lt;th&gt;p10&lt;/th&gt;&lt;/tr&gt;&lt;/thead&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td&gt;4-4-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-4-1-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-2-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-3-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-1-4-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-1-3-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-1-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-3&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;rwf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;lwf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-5-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-2-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-1-3&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;rwf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;lwf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-3&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;rwf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;lwf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-1-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-2-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-5-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-5-1-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;5-3-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb5&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;lb5&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;5-4-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb5&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;lb5&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-4-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-1-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-2-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-1-3-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-1-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-1-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-5-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;5-3-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb5&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;lb5&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-3-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-4-0&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rw&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lw&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;4-2-2-0&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb&lt;/td&gt;&lt;td&gt;rcb&lt;/td&gt;&lt;td&gt;lcb&lt;/td&gt;&lt;td&gt;lb&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-4-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rwb&lt;/td&gt;&lt;td&gt;rcmf&lt;/td&gt;&lt;td&gt;lcmf&lt;/td&gt;&lt;td&gt;lwb&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;5-3-0&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rb5&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;lb5&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;td&gt;esp&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-3-3-1&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rcmf3&lt;/td&gt;&lt;td&gt;dmf&lt;/td&gt;&lt;td&gt;lcmf3&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;3-2-3-2&lt;/td&gt;&lt;td&gt;gk&lt;/td&gt;&lt;td&gt;rcb3&lt;/td&gt;&lt;td&gt;cb&lt;/td&gt;&lt;td&gt;lcb3&lt;/td&gt;&lt;td&gt;rdmf&lt;/td&gt;&lt;td&gt;ldmf&lt;/td&gt;&lt;td&gt;ramf&lt;/td&gt;&lt;td&gt;amf&lt;/td&gt;&lt;td&gt;lamf&lt;/td&gt;&lt;td&gt;ss&lt;/td&gt;&lt;td&gt;cf&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt; | [optional] 
**start_sec** | **int** | The absolute second from the tagged video in which the formation started being used | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 
**team_id** | **int** | Team ID for the current formation which it belongs to | [optional] 

## Example

```python
from openapi_client.models.match_formation import MatchFormation

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFormation from a JSON string
match_formation_instance = MatchFormation.from_json(json)
# print the JSON string representation of the object
print(MatchFormation.to_json())

# convert the object into a dict
match_formation_dict = match_formation_instance.to_dict()
# create an instance of MatchFormation from a dict
match_formation_from_dict = MatchFormation.from_dict(match_formation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

