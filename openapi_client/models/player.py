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
from openapi_client.models.area import Area
from openapi_client.models.main_role import MainRole
from openapi_client.models.team import Team
from typing import Optional, Set
from typing_extensions import Self

class Player(BaseModel):
    """
    Retrieves information about a given player
    """ # noqa: E501
    birth_area: Optional[Area] = Field(default=None, alias="birthArea")
    birth_date: Optional[StrictStr] = Field(default=None, alias="birthDate")
    current_national_team_id: Optional[StrictInt] = Field(default=None, description="Unique ID of the national team this player is currently playing for (if exists)", alias="currentNationalTeamId")
    current_team: Optional[Team] = Field(default=None, description="Available with querystring param `details=currentTeam`", alias="currentTeam")
    current_team_id: Optional[StrictInt] = Field(default=None, description="Unique ID of the club team this player is currently playing for", alias="currentTeamId")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    foot: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Foot</th><th>Description</th></tr></thead><tbody><tr><td>right</td><td>Uses right foot as main foot</td></tr><tr><td>left</td><td>Uses left foot as main foot</td></tr><tr><td>both</td><td>Uses both left and right foot indifferently</td></tr></tbody></table>")
    gender: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Gender</th></tr></thead><tbody><tr><td>male</td></tr><tr><td>female</td></tr></tbody></table>")
    gsm_id: Optional[StrictInt] = Field(default=None, description="This field is no more used and it will be soon deprecated", alias="gsmId")
    height: Optional[StrictInt] = None
    image_data_url: Optional[StrictStr] = Field(default=None, description="Player picture URL", alias="imageDataURL")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    middle_name: Optional[StrictStr] = Field(default=None, alias="middleName")
    passport_area: Optional[Area] = Field(default=None, alias="passportArea")
    role: Optional[MainRole] = None
    short_name: Optional[StrictStr] = Field(default=None, alias="shortName")
    status: Optional[StrictStr] = Field(default=None, description="<table><thead><tr><th>Status</th><th>Description</th></tr></thead><tbody><tr><td>active</td><td>The player is currently active</td></tr><tr><td>retired</td><td>The player has retired</td></tr><tr><td>died</td><td>The player is dead</td></tr></tbody></table>")
    weight: Optional[StrictInt] = None
    wy_id: Optional[StrictInt] = Field(default=None, alias="wyId")
    __properties: ClassVar[List[str]] = ["birthArea", "birthDate", "currentNationalTeamId", "currentTeam", "currentTeamId", "firstName", "foot", "gender", "gsmId", "height", "imageDataURL", "lastName", "middleName", "passportArea", "role", "shortName", "status", "weight", "wyId"]

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
        """Create an instance of Player from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of birth_area
        if self.birth_area:
            _dict['birthArea'] = self.birth_area.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_team
        if self.current_team:
            _dict['currentTeam'] = self.current_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passport_area
        if self.passport_area:
            _dict['passportArea'] = self.passport_area.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Player from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "birthArea": Area.from_dict(obj["birthArea"]) if obj.get("birthArea") is not None else None,
            "birthDate": obj.get("birthDate"),
            "currentNationalTeamId": obj.get("currentNationalTeamId"),
            "currentTeam": Team.from_dict(obj["currentTeam"]) if obj.get("currentTeam") is not None else None,
            "currentTeamId": obj.get("currentTeamId"),
            "firstName": obj.get("firstName"),
            "foot": obj.get("foot"),
            "gender": obj.get("gender"),
            "gsmId": obj.get("gsmId"),
            "height": obj.get("height"),
            "imageDataURL": obj.get("imageDataURL"),
            "lastName": obj.get("lastName"),
            "middleName": obj.get("middleName"),
            "passportArea": Area.from_dict(obj["passportArea"]) if obj.get("passportArea") is not None else None,
            "role": MainRole.from_dict(obj["role"]) if obj.get("role") is not None else None,
            "shortName": obj.get("shortName"),
            "status": obj.get("status"),
            "weight": obj.get("weight"),
            "wyId": obj.get("wyId")
        })
        return _obj


