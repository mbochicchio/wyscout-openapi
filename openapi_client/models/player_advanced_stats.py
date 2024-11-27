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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.competition import Competition
from openapi_client.models.player import Player
from openapi_client.models.player_advanced_stats_average import PlayerAdvancedStatsAverage
from openapi_client.models.player_advanced_stats_percent import PlayerAdvancedStatsPercent
from openapi_client.models.player_advanced_stats_position import PlayerAdvancedStatsPosition
from openapi_client.models.player_advanced_stats_total import PlayerAdvancedStatsTotal
from openapi_client.models.round import Round
from openapi_client.models.season import Season
from typing import Optional, Set
from typing_extensions import Self

class PlayerAdvancedStats(BaseModel):
    """
    Returns advanced statistics of a given player in a specific competition season. Overall, the statistics provided are relative to the selected season, and not to a specific team
    """ # noqa: E501
    average: Optional[PlayerAdvancedStatsAverage] = None
    competition: Optional[Competition] = Field(default=None, description="Available with querystring param `fetch=competition`")
    competition_id: Optional[StrictInt] = Field(default=None, alias="competitionId")
    percent: Optional[PlayerAdvancedStatsPercent] = None
    player: Optional[Player] = Field(default=None, description="Available with querystring param `details=player`")
    player_id: Optional[StrictInt] = Field(default=None, alias="playerId")
    positions: Optional[List[PlayerAdvancedStatsPosition]] = None
    round: Optional[Round] = Field(default=None, description="Available with querystring param `fetch=round`")
    round_id: Optional[StrictInt] = Field(default=None, alias="roundId")
    season: Optional[Season] = Field(default=None, description="Available with querystring param `fetch=season`")
    season_id: Optional[StrictInt] = Field(default=None, alias="seasonId")
    total: Optional[PlayerAdvancedStatsTotal] = None
    __properties: ClassVar[List[str]] = ["average", "competition", "competitionId", "percent", "player", "playerId", "positions", "round", "roundId", "season", "seasonId", "total"]

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
        """Create an instance of PlayerAdvancedStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of average
        if self.average:
            _dict['average'] = self.average.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competition
        if self.competition:
            _dict['competition'] = self.competition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of percent
        if self.percent:
            _dict['percent'] = self.percent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of player
        if self.player:
            _dict['player'] = self.player.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item_positions in self.positions:
                if _item_positions:
                    _items.append(_item_positions.to_dict())
            _dict['positions'] = _items
        # override the default output from pydantic by calling `to_dict()` of round
        if self.round:
            _dict['round'] = self.round.to_dict()
        # override the default output from pydantic by calling `to_dict()` of season
        if self.season:
            _dict['season'] = self.season.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total
        if self.total:
            _dict['total'] = self.total.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlayerAdvancedStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "average": PlayerAdvancedStatsAverage.from_dict(obj["average"]) if obj.get("average") is not None else None,
            "competition": Competition.from_dict(obj["competition"]) if obj.get("competition") is not None else None,
            "competitionId": obj.get("competitionId"),
            "percent": PlayerAdvancedStatsPercent.from_dict(obj["percent"]) if obj.get("percent") is not None else None,
            "player": Player.from_dict(obj["player"]) if obj.get("player") is not None else None,
            "playerId": obj.get("playerId"),
            "positions": [PlayerAdvancedStatsPosition.from_dict(_item) for _item in obj["positions"]] if obj.get("positions") is not None else None,
            "round": Round.from_dict(obj["round"]) if obj.get("round") is not None else None,
            "roundId": obj.get("roundId"),
            "season": Season.from_dict(obj["season"]) if obj.get("season") is not None else None,
            "seasonId": obj.get("seasonId"),
            "total": PlayerAdvancedStatsTotal.from_dict(obj["total"]) if obj.get("total") is not None else None
        })
        return _obj


