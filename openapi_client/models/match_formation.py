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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.players_list_inner import PlayersListInner
from openapi_client.models.team import Team
from typing import Optional, Set
from typing_extensions import Self

class MatchFormation(BaseModel):
    """
    Team formation about a given match
    """ # noqa: E501
    end_sec: Optional[StrictInt] = Field(default=None, description="The absolute second from the tagged video in which the formation finished being used", alias="endSec")
    id: Optional[StrictInt] = None
    match_period_end: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Period</th><th>Description</th></tr></thead><tbody><tr><td>1H</td><td>First Half Time</td></tr><tr><td>2H</td><td>Second Half Time</td></tr><tr><td>E1</td><td>First Extra Time</td></tr><tr><td>E2</td><td>Second Extra Time</td></tr></tbody></table>", alias="matchPeriodEnd")
    match_period_start: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Period</th><th>Description</th></tr></thead><tbody><tr><td>1H</td><td>First Half Time</td></tr><tr><td>2H</td><td>Second Half Time</td></tr><tr><td>E1</td><td>First Extra Time</td></tr><tr><td>E2</td><td>Second Extra Time</td></tr></tbody></table>", alias="matchPeriodStart")
    players: Optional[List[PlayersListInner]] = Field(default=None, description="List of players in the current formation")
    players_on_field: Optional[StrictInt] = Field(default=None, description="The current amount of players present on the field", alias="playersOnField")
    scheme: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Scheme</th><th>p0</th><th>p1</th><th>p2</th><th>p3</th><th>p4</th><th>p5</th><th>p6</th><th>p7</th><th>p8</th><th>p9</th><th>p10</th></tr></thead><tbody><tr><td>4-4-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>ss</td><td>cf</td></tr><tr><td>4-4-1-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>amf</td><td>cf</td></tr><tr><td>4-3-2-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>amf</td><td>amf</td><td>cf</td></tr><tr><td>4-2-3-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>ramf</td><td>amf</td><td>lamf</td><td>cf</td></tr><tr><td>4-1-4-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>dmf</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>cf</td></tr><tr><td>4-1-3-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>dmf</td><td>ramf</td><td>amf</td><td>lamf</td><td>ss</td><td>cf</td></tr><tr><td>4-3-1-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>amf</td><td>ss</td><td>cf</td></tr><tr><td>4-3-3</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>rwf</td><td>cf</td><td>lwf</td></tr><tr><td>4-5-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rw</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>lw</td><td>cf</td></tr><tr><td>4-2-2-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>ramf</td><td>lamf</td><td>ss</td><td>cf</td></tr><tr><td>4-2-1-3</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>amf</td><td>rwf</td><td>cf</td><td>lwf</td></tr><tr><td>3-4-3</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>rwf</td><td>cf</td><td>lwf</td></tr><tr><td>3-4-1-2</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>amf</td><td>ss</td><td>cf</td></tr><tr><td>3-4-2-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>amf</td><td>amf</td><td>cf</td></tr><tr><td>3-5-2</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>lwb</td><td>ss</td><td>cf</td></tr><tr><td>3-5-1-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rw</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>lw</td><td>amf</td><td>cf</td></tr><tr><td>5-3-2</td><td>gk</td><td>rb5</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>lb5</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>ss</td><td>cf</td></tr><tr><td>5-4-1</td><td>gk</td><td>rb5</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>lb5</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>cf</td></tr><tr><td>4-3-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>ss</td><td>cf</td><td>esp</td></tr><tr><td>4-4-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>cf</td><td>esp</td></tr><tr><td>4-3-1-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>amf</td><td>cf</td><td>esp</td></tr><tr><td>4-2-2-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>amf</td><td>amf</td><td>cf</td><td>esp</td></tr><tr><td>4-1-3-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>dmf</td><td>ramf</td><td>amf</td><td>lamf</td><td>cf</td><td>esp</td></tr><tr><td>4-2-1-2</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>amf</td><td>ss</td><td>cf</td><td>esp</td></tr><tr><td>3-4-2</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>ss</td><td>cf</td><td>esp</td></tr><tr><td>3-4-1-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>amf</td><td>cf</td><td>esp</td></tr><tr><td>3-5-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>lwb</td><td>cf</td><td>esp</td></tr><tr><td>5-3-1</td><td>gk</td><td>rb5</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>lb5</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>cf</td><td>esp</td></tr><tr><td>4-3-1</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>cf</td><td>esp</td><td>esp</td></tr><tr><td>4-4-0</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rw</td><td>rcmf</td><td>lcmf</td><td>lw</td><td>esp</td><td>esp</td></tr><tr><td>4-2-2-0</td><td>gk</td><td>rb</td><td>rcb</td><td>lcb</td><td>lb</td><td>rdmf</td><td>ldmf</td><td>amf</td><td>amf</td><td>esp</td><td>esp</td></tr><tr><td>3-4-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rwb</td><td>rcmf</td><td>lcmf</td><td>lwb</td><td>cf</td><td>esp</td><td>esp</td></tr><tr><td>5-3-0</td><td>gk</td><td>rb5</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>lb5</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>esp</td><td>esp</td></tr><tr><td>3-3-3-1</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rcmf3</td><td>dmf</td><td>lcmf3</td><td>ramf</td><td>amf</td><td>lamf</td><td>cf</td></tr><tr><td>3-2-3-2</td><td>gk</td><td>rcb3</td><td>cb</td><td>lcb3</td><td>rdmf</td><td>ldmf</td><td>ramf</td><td>amf</td><td>lamf</td><td>ss</td><td>cf</td></tr></tbody></table>")
    start_sec: Optional[StrictInt] = Field(default=None, description="The absolute second from the tagged video in which the formation started being used", alias="startSec")
    team: Optional[Team] = None
    team_id: Optional[StrictInt] = Field(default=None, description="Team ID for the current formation which it belongs to", alias="teamId")
    __properties: ClassVar[List[str]] = ["endSec", "id", "matchPeriodEnd", "matchPeriodStart", "players", "playersOnField", "scheme", "startSec", "team", "teamId"]

    @field_validator('match_period_end')
    def match_period_end_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1H', '2H', 'E1', 'E2']):
            raise ValueError("must be one of enum values ('1H', '2H', 'E1', 'E2')")
        return value

    @field_validator('match_period_start')
    def match_period_start_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['1H', '2H', 'E1', 'E2']):
            raise ValueError("must be one of enum values ('1H', '2H', 'E1', 'E2')")
        return value

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
        """Create an instance of MatchFormation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in players (list)
        _items = []
        if self.players:
            for _item_players in self.players:
                if _item_players:
                    _items.append(_item_players.to_dict())
            _dict['players'] = _items
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatchFormation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endSec": obj.get("endSec"),
            "id": obj.get("id"),
            "matchPeriodEnd": obj.get("matchPeriodEnd"),
            "matchPeriodStart": obj.get("matchPeriodStart"),
            "players": [PlayersListInner.from_dict(_item) for _item in obj["players"]] if obj.get("players") is not None else None,
            "playersOnField": obj.get("playersOnField"),
            "scheme": obj.get("scheme"),
            "startSec": obj.get("startSec"),
            "team": Team.from_dict(obj["team"]) if obj.get("team") is not None else None,
            "teamId": obj.get("teamId")
        })
        return _obj


