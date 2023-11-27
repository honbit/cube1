# Dynamic data models: https://cube.dev/docs/product/data-modeling/dynamic

from cube import TemplateContext

template = TemplateContext()

# Python functions can be registered so that they are callable from Jinja.
# See '{{ is_accessible_by_team(...) }}' in `views/customers.yml'.
# Learn more: https://cube.dev/docs/product/data-modeling/dynamic/jinja#python
@template.function('is_accessible_by_team')
def is_accessible_by_team(team: str, ctx: dict) -> bool:
  return team == ctx['securityContext'].setdefault('team', 'default')




# from cube_dbt import Dbt

# template = TemplateContext()

# manifest_url = 'https://cube-dbt-integration.s3.amazonaws.com/manifest.json'

# dbt = Dbt.from_url(manifest_url).filter(paths=['marts/'])

# for model in dbt.models:
#   print(f"aaaa {model.name}")

# @template.function('dbt_models')
# def dbt_models():
#   return dbt.models

# @template.function('dbt_model')
# def dbt_model(name):
#   return dbt.model(name)


