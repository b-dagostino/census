# generated by datamodel-codegen:
#   filename:  https://project-open-data.cio.gov/v1.1/schema/catalog.json
#   timestamp: 2024-09-07T00:13:26+00:00

from __future__ import annotations

import asyncio
from datetime import date
from enum import Enum
from typing import List, Optional, Self, Union

from aiohttp import ClientSession
from pydantic import AnyUrl, BaseModel, ConfigDict, Field, PrivateAttr, RootModel

from census.utils import get_json_from_url


class FieldType(Enum):
    dcat_Catalog = "dcat:Catalog"


class ConformsTo(Enum):
    https___project_open_data_cio_gov_v1_1_schema = (
        "https://project-open-data.cio.gov/v1.1/schema"
    )


class FieldType1(Enum):
    dcat_Dataset = "dcat:Dataset"


class AccessLevel(Enum):
    public = "public"
    restricted_public = "restricted public"
    non_public = "non-public"


class Rights(RootModel[str]):
    root: str = Field(
        ...,
        description='This may include information regarding access or restrictions based on privacy, security, or other policies. This should also provide an explanation for the selected "accessLevel" including instructions for how to access a restricted file, if applicable, or explanation for why a "non-public" or "restricted public" data assetis not "public," if applicable. Text, 255 characters.',
        max_length=255,
        min_length=1,
        title="Rights",
    )


class AccrualPeriodicity(Enum):
    irregular = "irregular"


class AccrualPeriodicity1(RootModel[str]):
    root: str = Field(
        ...,
        description="Frequency with which dataset is published.",
        pattern="^R\\/P(?:\\d+(?:\\.\\d+)?Y)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
        title="Frequency",
    )


class BureauCodeItem(RootModel[str]):
    root: str = Field(..., pattern="[0-9]{3}:[0-9]{2}")


class DescribedByType(RootModel[str]):
    root: str = Field(
        ...,
        description="The machine-readable file format (IANA Media Type or MIME Type) of the distributions describedBy URL",
        pattern="^[-\\w]+/[-\\w]+(\\.[-\\w]+)*([+][-\\w]+)?$",
        title="Data Dictionary Type",
    )


class Issued(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="Date of formal issuance.",
        pattern="^([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
        title="Release Date",
    )


class KeywordItem(RootModel[str]):
    root: str = Field(..., min_length=1)


class LanguageItem(RootModel[str]):
    root: str = Field(
        ...,
        pattern="^(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-(x(-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+)|((en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE)|(art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu|zh-hakka|zh-min|zh-min-nan|zh-xiang)))$",
    )


class Modified(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="Most recent date on which the dataset was changed, updated or modified.",
        pattern="^([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
        title="Last Update",
    )


class Modified1(RootModel[str]):
    root: str = Field(
        ...,
        description="Most recent date on which the dataset was changed, updated or modified.",
        pattern="^(R\\d*\\/)?P(?:\\d+(?:\\.\\d+)?Y)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
        title="Last Update",
    )


class Modified2(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="Most recent date on which the dataset was changed, updated or modified.",
        pattern="^(R\\d*\\/)?([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\4([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\18[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?(\\/)P(?:\\d+(?:\\.\\d+)?Y)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
        title="Last Update",
    )


class PrimaryITInvestmentUII(RootModel[str]):
    root: str = Field(
        ...,
        description="For linking a dataset with an IT Unique Investment Identifier (UII)",
        pattern="[0-9]{3}-[0-9]{9}",
        title="Primary IT Investment UII",
    )


class ProgramCodeItem(RootModel[str]):
    root: str = Field(..., pattern="[0-9]{3}:[0-9]{3}")


class References(RootModel[List[AnyUrl]]):
    root: List[AnyUrl] = Field(
        ...,
        description="Related documents such as technical information about a dataset, developer documentation, etc.",
        title="Related Documents",
    )


class Spatial(RootModel[str]):
    root: str = Field(
        ...,
        description="The range of spatial applicability of a dataset. Could include a spatial region like a bounding box or a named place.",
        min_length=1,
        title="Spatial",
    )


class SystemOfRecords(RootModel[str]):
    root: str = Field(
        ...,
        description="If the systems is designated as a system of records under the Privacy Act of 1974, provide the URL to the System of Records Notice related to this dataset.",
        min_length=1,
        title="System of Records",
    )


class Temporal(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data).",
        pattern="^([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?(\\/)([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\3([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\17[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
        title="Temporal",
    )


class Temporal1(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data).",
        pattern="^(R\\d*\\/)?([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\4([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\18[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?(\\/)P(?:\\d+(?:\\.\\d+)?Y)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
        title="Temporal",
    )


class Temporal2(RootModel[str]):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    root: str = Field(
        ...,
        description="The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data).",
        pattern="^(R\\d*\\/)?P(?:\\d+(?:\\.\\d+)?Y)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?\\/([\\+-]?\\d{4}(?!\\d{2}\\b))((-?)((0[1-9]|1[0-2])(\\4([12]\\d|0[1-9]|3[01]))?|W([0-4]\\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\\d|[12]\\d{2}|3([0-5]\\d|6[1-6])))([T\\s]((([01]\\d|2[0-3])((:?)[0-5]\\d)?|24\\:?00)([\\.,]\\d+(?!:))?)?(\\18[0-5]\\d([\\.,]\\d+)?)?([zZ]|([\\+-])([01]\\d|2[0-3]):?([0-5]\\d)?)?)?)?$",
        title="Temporal",
    )


class IsPartOf(RootModel[str]):
    root: str = Field(
        ...,
        description="The collection of which the dataset is a subset",
        min_length=1,
        title="Collection",
    )


class ThemeItem(RootModel[str]):
    root: str = Field(..., min_length=1)


class Theme(RootModel[List[ThemeItem]]):
    root: List[ThemeItem] = Field(
        ...,
        description="Main thematic category of the dataset.",
        min_length=1,
        title="Category",
    )


class FieldType2(Enum):
    vcard_Contact = "vcard:Contact"


class Vcard(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_type: Optional[FieldType2] = Field(
        None,
        alias="@type",
        description="IRI for the JSON-LD data type. This should be vcard:Contact for contactPoint",
        title="Metadata Context",
    )
    fn: str = Field(
        ...,
        description="A full formatted name, eg Firstname Lastname",
        min_length=1,
        title="Contact Name",
    )
    hasEmail: str = Field(
        ...,
        description="Email address for the contact",
        # pattern="^mailto:[\\w\\_\\~\\!\\$\\&\\'\\(\\)\\*\\+\\,\\;\\=\\:.-]+@[\\w.-]+\\.[\\w.-]+?$",
        title="Email",
    )


class FieldType3(Enum):
    dcat_Distribution = "dcat:Distribution"


class MediaType(RootModel[str]):
    root: str = Field(
        ...,
        description="The machine-readable file format (IANA Media Type or MIME Type) of the distribution�s downloadURL",
        pattern="^[-\\w]+/[-\\w]+(\\.[-\\w]+)*([+][-\\w]+)?$",
        title="Media Type",
    )


class Format(RootModel[str]):
    root: str = Field(
        ...,
        description="A human-readable description of the file format of a distribution",
        min_length=1,
        title="Format",
    )


class Description(RootModel[str]):
    root: str = Field(
        ...,
        description="Human-readable description of the distribution",
        min_length=1,
        title="Description",
    )


class Title(RootModel[str]):
    root: str = Field(
        ...,
        description="Human-readable name of the distribution",
        min_length=1,
        title="Title",
    )


class Distribution(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_type: Optional[FieldType3] = Field(
        None,
        alias="@type",
        description="IRI for the JSON-LD data type. This should be dcat:Distribution for each Distribution",
        title="Metadata Context",
    )
    downloadURL: Optional[AnyUrl] = Field(
        None,
        description="URL providing direct access to a downloadable file of a dataset",
        title="Download URL",
    )
    mediaType: Optional[MediaType] = Field(
        None,
        description="The machine-readable file format (IANA Media Type or MIME Type) of the distribution�s downloadURL",
        title="Media Type",
    )
    format: Optional[Format] = Field(
        None,
        description="A human-readable description of the file format of a distribution",
        title="Format",
    )
    accessURL: Optional[AnyUrl] = Field(
        None,
        description="URL providing indirect access to a dataset",
        title="Access URL",
    )
    description: Optional[Description] = Field(
        None,
        description="Human-readable description of the distribution",
        title="Description",
    )
    title: Optional[Title] = Field(
        None, description="Human-readable name of the distribution", title="Title"
    )
    conformsTo: Optional[AnyUrl] = Field(
        None,
        description="URL providing indirect access to a dataset",
        title="Data Standard",
    )
    describedBy: Optional[AnyUrl] = Field(
        None,
        description="URL to the data dictionary for the distribution found at the downloadURL",
        title="Data Dictionary",
    )
    describedByType: Optional[DescribedByType] = Field(
        None,
        description="The machine-readable file format (IANA Media Type or MIME Type) of the distribution�s describedBy URL",
        title="Data Dictionary Type",
    )


class FieldType4(Enum):
    org_Organization = "org:Organization"


class Organization(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_type: Optional[FieldType4] = Field(
        None,
        alias="@type",
        description="IRI for the JSON-LD data type. This should be org:Organization for each publisher",
        title="Metadata Context",
    )
    name: str = Field(
        ...,
        description="A full formatted name, eg Firstname Lastname",
        min_length=1,
        title="Publisher Name",
    )
    subOrganizationOf: Optional[Organization] = Field(None, title="Parent Organization")


class Dataset(BaseModel, extra="forbid"):
    c_dataset: list[str]
    c_documentationLink: AnyUrl
    c_examplesLink: AnyUrl
    c_geographyLink: AnyUrl
    c_groupsLink: AnyUrl
    c_isAggregate: bool | None = Field(None)
    c_isAvailable: bool
    c_isCube: bool | None = Field(None)
    c_isMicrodata: Optional[bool] = Field(None)
    c_isTimeseries: bool | None = Field(None)
    c_sorts_url: AnyUrl
    c_tagsLink: AnyUrl
    c_variablesLink: AnyUrl
    c_vintage: int = Field(None)
    field_type: Optional[FieldType1] = Field(
        None,
        alias="@type",
        description="IRI for the JSON-LD data type. This should be dcat:Dataset for each Dataset",
        title="Metadata Context",
    )
    accessLevel: AccessLevel = Field(
        ...,
        description="The degree to which this dataset could be made publicly-available, regardless of whether it has been made available. Choices: public (Data asset is or could be made publicly available to all without restrictions), restricted public (Data asset is available under certain use restrictions), or non-public (Data asset is not available to members of the public)",
        title="Public Access Level",
    )
    rights: Optional[Rights] = Field(
        None,
        description='This may include information regarding access or restrictions based on privacy, security, or other policies. This should also provide an explanation for the selected "accessLevel" including instructions for how to access a restricted file, if applicable, or explanation for why a "non-public" or "restricted public" data assetis not "public," if applicable. Text, 255 characters.',
        title="Rights",
    )
    accrualPeriodicity: Optional[Union[AccrualPeriodicity, AccrualPeriodicity1]] = (
        Field(
            None,
            description="Frequency with which dataset is published.",
            title="Frequency",
        )
    )
    bureauCode: List[BureauCodeItem] = Field(
        ...,
        description='Federal agencies, combined agency and bureau code from <a href="http://www.whitehouse.gov/sites/default/files/omb/assets/a11_current_year/app_c.pdf">OMB Circular A-11, Appendix C</a> in the format of <code>015:010</code>.',
        min_length=1,
        title="Bureau Code",
    )
    contactPoint: Vcard
    describedBy: Optional[AnyUrl] = Field(
        None,
        description="URL to the data dictionary for the dataset or API. Note that documentation other than a data dictionary can be referenced using Related Documents as shown in the expanded fields.",
        title="Data Dictionary",
    )
    describedByType: Optional[DescribedByType] = Field(
        None,
        description="The machine-readable file format (IANA Media Type or MIME Type) of the distribution�s describedBy URL",
        title="Data Dictionary Type",
    )
    conformsTo: Optional[AnyUrl] = Field(
        None,
        description="URI used to identify a standardized specification the dataset conforms to",
        title="Data Standard",
    )
    dataQuality: Optional[bool] = Field(
        None,
        description="Whether the dataset meets the agency�s Information Quality Guidelines (true/false).",
        title="Data Quality",
    )
    description: str = Field(
        ...,
        description="Human-readable description (e.g., an abstract) with sufficient detail to enable a user to quickly understand whether the asset is of interest.",
        min_length=1,
        title="Description",
    )
    distribution: Optional[List[Distribution]] = Field(
        None,
        description="A container for the array of Distribution objects",
        title="Distribution",
    )
    identifier: str = Field(
        ...,
        description="A unique identifier for the dataset or API as maintained within an Agency catalog or database.",
        min_length=1,
        title="Unique Identifier",
    )
    issued: Optional[Issued] = Field(
        None, description="Date of formal issuance.", title="Release Date"
    )
    keyword: List[KeywordItem] = Field(
        ...,
        description="Tags (or keywords) help users discover your dataset; please include terms that would be used by technical and non-technical users.",
        min_length=1,
        title="Tags",
    )
    landingPage: Optional[AnyUrl] = Field(
        None,
        description="Alternative landing page used to redirect user to a contextual, Agency-hosted �homepage� for the Dataset or API when selecting this resource from the Data.gov user interface.",
        title="Homepage URL",
    )
    language: Optional[List[LanguageItem]] = Field(
        None, description="The language of the dataset.", title="Language"
    )
    license: Optional[AnyUrl] = Field(
        None,
        description='The license dataset or API is published with. See <a href="https://project-open-data.cio.gov/open-licenses/">Open Licenses</a> for more information.',
        title="License",
    )
    modified: Union[Modified, Modified1, Modified2] = Field(
        ...,
        description="Most recent date on which the dataset was changed, updated or modified.",
        title="Last Update",
    )
    primaryITInvestmentUII: Optional[PrimaryITInvestmentUII] = Field(
        None,
        description="For linking a dataset with an IT Unique Investment Identifier (UII)",
        title="Primary IT Investment UII",
    )
    programCode: List[ProgramCodeItem] = Field(
        ...,
        description='Federal agencies, list the primary program related to this data asset, from the <a href="http://goals.performance.gov/sites/default/files/images/FederalProgramInventory_FY13_MachineReadable_091613.xls">Federal Program Inventory</a>. Use the format of <code>015:001</code>',
        min_length=1,
        title="Program Code",
    )
    publisher: Organization
    references: Optional[References] = Field(
        None,
        description="Related documents such as technical information about a dataset, developer documentation, etc.",
        title="Related Documents",
    )
    spatial: Optional[Spatial] = Field(
        None,
        description="The range of spatial applicability of a dataset. Could include a spatial region like a bounding box or a named place.",
        title="Spatial",
    )
    systemOfRecords: Optional[SystemOfRecords] = Field(
        None,
        description="If the systems is designated as a system of records under the Privacy Act of 1974, provide the URL to the System of Records Notice related to this dataset.",
        title="System of Records",
    )
    temporal: Optional[Union[Temporal, Temporal1, Temporal2]] = Field(
        None,
        description="The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data).",
        title="Temporal",
    )
    isPartOf: Optional[IsPartOf] = Field(
        None,
        description="The collection of which the dataset is a subset",
        title="Collection",
    )
    theme: Optional[Theme] = Field(
        None, description="Main thematic category of the dataset.", title="Category"
    )
    title: str = Field(
        ...,
        description="Human-readable name of the asset. Should be in plain English and include sufficient detail to facilitate search and discovery.",
        min_length=1,
        title="Title",
    )

    _variables: Variables | None = PrivateAttr(None)
    _geography: Geography | None = PrivateAttr(None)

    @property
    def variables(self) -> Variables | None:
        return self._variables

    @property
    def geography(self) -> Geography | None:
        return self._geography

    async def get_variables(self, session: ClientSession) -> None:
        if self._variables is not None:
            return

        async with session.get(str(self.c_variablesLink)) as r:
            var_json = await r.json()
            self._variables = Variables(**var_json)

    async def get_geography(self, session: ClientSession) -> None:
        if self._geography is not None:
            return

        async with session.get(str(self.c_geographyLink)) as r:
            geo_json = await r.json()
            self._geography = Geography(**geo_json)


class ProjectOpenDataCatalog(BaseModel):
    model_config = ConfigDict(
        extra="allow",
    )
    field_context: Optional[AnyUrl] = Field(
        None,
        alias="@context",
        description="URL or JSON object for the JSON-LD Context that defines the schema used",
        title="Metadata Context",
    )
    field_id: Optional[AnyUrl] = Field(
        None,
        alias="@id",
        description="IRI for the JSON-LD Node Identifier of the Catalog. This should be the URL of the data.json file itself.",
        title="Metadata Catalog ID",
    )
    field_type: Optional[FieldType] = Field(
        None,
        alias="@type",
        description="IRI for the JSON-LD data type. This should be dcat:Catalog for the Catalog",
        title="Metadata Context",
    )
    conformsTo: ConformsTo = Field(
        ..., description="Version of Schema", title="Version of Schema"
    )
    describedBy: Optional[AnyUrl] = Field(
        None,
        description="URL for the JSON Schema file that defines the schema used",
        title="Data Dictionary",
    )
    dataset: List[Dataset]

    async def get_dataset_variables_and_geography(self):
        async def get_dataset_vars_and_geo(session: ClientSession, dataset: Dataset):
            await dataset.get_variables(session)
            await dataset.get_geography(session)

        async with ClientSession() as session:
            await asyncio.gather(
                *(
                    asyncio.ensure_future(get_dataset_vars_and_geo(session, dataset))
                    for dataset in self.dataset
                )
            )

    @classmethod
    def from_url(cls: type[Self], url: str) -> Self:
        return cls(**get_json_from_url(url))


Organization.model_rebuild()


class Default(BaseModel, extra="forbid"):
    isDefault: bool


class Fips(BaseModel, extra="forbid"):
    geoLevelDisplay: str = Field(None)
    geoLevelId: str | None = Field(None)
    limit: str | None = Field(None)
    name: str
    optionalWithWCFor: str | None = Field(None)
    referenceDate: str | None = Field(None)
    requires: list[str] | None = Field(None)
    wildcard: list[str] | bool | None = Field(None)


class Geography(BaseModel, extra="forbid"):
    default: list[Default] | None = Field(None)
    fips: list[Fips] | None = Field(None)


class Range(BaseModel, extra="forbid", frozen=True):
    min: str
    max: str
    description: str


class Values(BaseModel, extra="forbid", frozen=True):
    item: dict[str, str] | None = Field(None)
    range: list[Range] | None = Field(None)

    def __hash__(self) -> int:
        return (
            hash((*self.item.items(), self.range))
            if self.item is not None
            else hash((self.item, self.range))
        )


class Variable(BaseModel, extra="forbid", frozen=True):
    attributes: str | None = Field(None)
    concept: str | None = Field(None)
    datetime: dict | None = Field(None)
    group: str
    hasGeoCollectionSupport: bool | None = Field(None)
    isWeight: bool | None = Field(None, alias="is-weight")
    label: str
    limit: int
    predicateOnly: bool | None = Field(None)
    predicateType: str | None = Field(None)
    required: str | None = Field(None)
    suggestedWeight: str | None = Field(None, alias="suggested-weight")
    values: Values | None = Field(None)

    def __hash__(self) -> int:
        return hash(
            (
                self.attributes,
                self.concept,
                # self.datetime,
                self.group,
                self.hasGeoCollectionSupport,
                self.isWeight,
                self.label,
                self.limit,
                self.predicateOnly,
                self.predicateType,
                self.required,
                self.suggestedWeight,
                self.values,
            )
        )


class Variables(BaseModel, extra="forbid"):
    variables: dict[str, Variable]
