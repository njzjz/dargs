## Generate JSON schema from an argument

One can use {func}`dargs.json_schema_generate_json_schema` to generate [JSON schema](https://json-schema.org/).

```py
import json

from dargs import Argument
from dargs.json_schema import generate_json_schema
from deepmd.utils.argcheck import gen_args


a = Argument("DeePMD-kit", dtype=dict, sub_fields=gen_args())
schema = generate_json_schema(a)
with open("deepmd.json", "w") as f:
    json.dump(schema, f, indent=2)
```

JSON schema can be used in several JSON editors. For example, in [Visual Studio Code](https://code.visualstudio.com/), you can [configure JSON schema](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings) in the project `settings.json`:

```json
{
    "json.schemas": [
        {
            "fileMatch": [
                "/**/*.json"
            ],
            "url": "./deepmd.json"
        }
    ]
}
```