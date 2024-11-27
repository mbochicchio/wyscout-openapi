# coding: utf-8

"""
    Wyscout API (v4)

    [Customer resources](https://www.hudl.com/support/wyscout) | [Customer support](https://www.hudl.com/support/contact)  [Wyscout Data resources](https://footballdata.wyscout.com/resources/)  **IMPORTANT: Version switching planned for July 20th 2021.**  On July 20th 2021 we will switch v3 as the Current version. V2 will become Legacy.  Please see [Versioning](#section/Versioning) section for any related details.  # Overview  This is the product documentation for our API service, in which you can find all definitions and technical information you may need.  # Authentication  ## Overview  This page explain how to authenticate to Wyscout APIs using Basic Access Authentication.  ## Using your client software  Depending on your client software you should be provided with a mechanism for supplying an username and password: that will build the required authentication headers automatically.  For example you can specify the -u argument with curl as username:password.  ## Supplying Basic Access Authentication headers  It is possible to construct the authentication headers manually:  * Build a string of the form username:password. * Encode the string in Base64 * Supply an `Authorization` header with content `Basic` followed by the encoded string.   For example, the string `Aladdin:OpenSesame` encodes to `QWxhZGRpbjpPcGVuU2VzYW1l` in base64,   so you would use this string `Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l`  ## Rate limits  To avoid services overload requests are rate limited. The Wyscout API currently enforces a limit of **12** request per second per API Key.  If the rate limit is exceeded, the API will return the following HTTP 429 response:  ```json   {     \"error\": {       \"code\": 429,       \"message\": \"Too many requests\"     }   } ```  # Data glossary and definitions  At the following link you can find our Data Glossary that describes events, metrics and concepts used across the Wyscout API, Platform and reports.  <a href=\"https://dataglossary.wyscout.com/\" target=\"_blank\">Wyscout Data Glossary</a>   ## Pitch coordinates  ![Pitch map](assets/images/WyscoutDataCoordinates.png)  The event's coordinates depends on the subject. The subject's goal to be defended is always **x=0%** and the attack is always **x=100%**. All values are % expressed as **(x,y)**.  # Versioning  Wyscout gives you the chance to choose between three different sets of API endpoints.  ## Current The latest available version. It includes the most recent endpoints and improvements.  ## Preview The beta version of our next official release. Here we start to implement future improvements and new endpoints.  ## Legacy The old version. This is still available and running, in order to let users adapt their tools to new ones.  ## Version Switch  Wyscout will constantly improve its dataset by adding new endpoints and improving the existing ones. “Preview” version is where you can find last delivered updates. When a new and improved “Current” version is released, the previous version becomes “Legacy” – which means it will not immediately cease to exist, giving you the time to adapt your systems. It will be available and running until another new version – “Current” – is released, at least six months after the previous one.  ![Version Switch](assets/images/WyscoutVersionSwitch.png)  Documentation on [apidocs.wyscout.com](apidocs.wyscout.com) will always be available also for “Legacy” version. Each version will receive support as from the following table:  ![Version Support](assets/images/WyscoutVersionSupport.png)

    The version of the OpenAPI document: 2024-05-09T09:09:27Z
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MatchAdvancedStatsPossession(BaseModel):
    """
    MatchAdvancedStatsPossession
    """ # noqa: E501
    avg_possession_duration: Optional[StrictStr] = Field(default=None, alias="avgPossessionDuration")
    minutes_of_possession1_15: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession1-15")
    minutes_of_possession106_120: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession106-120")
    minutes_of_possession16_30: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession16-30")
    minutes_of_possession31_45: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession31-45")
    minutes_of_possession46_60: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession46-60")
    minutes_of_possession61_75: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession61-75")
    minutes_of_possession76_90: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession76-90")
    minutes_of_possession91_105: Optional[StrictStr] = Field(default=None, alias="minutesOfPossession91-105")
    possession1_15: Optional[StrictInt] = Field(default=None, alias="possession1-15")
    possession106_120: Optional[StrictInt] = Field(default=None, alias="possession106-120")
    possession16_30: Optional[StrictInt] = Field(default=None, alias="possession16-30")
    possession31_45: Optional[StrictInt] = Field(default=None, alias="possession31-45")
    possession46_60: Optional[StrictInt] = Field(default=None, alias="possession46-60")
    possession61_75: Optional[StrictInt] = Field(default=None, alias="possession61-75")
    possession76_90: Optional[StrictInt] = Field(default=None, alias="possession76-90")
    possession91_105: Optional[StrictInt] = Field(default=None, alias="possession91-105")
    possession_number: Optional[StrictInt] = Field(default=None, alias="possessionNumber")
    possession_percent: Optional[StrictInt] = Field(default=None, alias="possessionPercent")
    pure_possession_time: Optional[StrictStr] = Field(default=None, alias="purePossessionTime")
    reaching_opponent_box: Optional[StrictInt] = Field(default=None, alias="reachingOpponentBox")
    reaching_opponent_half: Optional[StrictInt] = Field(default=None, alias="reachingOpponentHalf")
    __properties: ClassVar[List[str]] = ["avgPossessionDuration", "minutesOfPossession1-15", "minutesOfPossession106-120", "minutesOfPossession16-30", "minutesOfPossession31-45", "minutesOfPossession46-60", "minutesOfPossession61-75", "minutesOfPossession76-90", "minutesOfPossession91-105", "possession1-15", "possession106-120", "possession16-30", "possession31-45", "possession46-60", "possession61-75", "possession76-90", "possession91-105", "possessionNumber", "possessionPercent", "purePossessionTime", "reachingOpponentBox", "reachingOpponentHalf"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MatchAdvancedStatsPossession from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchAdvancedStatsPossession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgPossessionDuration": obj.get("avgPossessionDuration"),
            "minutesOfPossession1-15": obj.get("minutesOfPossession1-15"),
            "minutesOfPossession106-120": obj.get("minutesOfPossession106-120"),
            "minutesOfPossession16-30": obj.get("minutesOfPossession16-30"),
            "minutesOfPossession31-45": obj.get("minutesOfPossession31-45"),
            "minutesOfPossession46-60": obj.get("minutesOfPossession46-60"),
            "minutesOfPossession61-75": obj.get("minutesOfPossession61-75"),
            "minutesOfPossession76-90": obj.get("minutesOfPossession76-90"),
            "minutesOfPossession91-105": obj.get("minutesOfPossession91-105"),
            "possession1-15": obj.get("possession1-15"),
            "possession106-120": obj.get("possession106-120"),
            "possession16-30": obj.get("possession16-30"),
            "possession31-45": obj.get("possession31-45"),
            "possession46-60": obj.get("possession46-60"),
            "possession61-75": obj.get("possession61-75"),
            "possession76-90": obj.get("possession76-90"),
            "possession91-105": obj.get("possession91-105"),
            "possessionNumber": obj.get("possessionNumber"),
            "possessionPercent": obj.get("possessionPercent"),
            "purePossessionTime": obj.get("purePossessionTime"),
            "reachingOpponentBox": obj.get("reachingOpponentBox"),
            "reachingOpponentHalf": obj.get("reachingOpponentHalf")
        })
        return _obj

