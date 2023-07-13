
from strawberry import Schema
from strawberry.tools import merge_types
from videos.schema import Query as QueryVideo , Mutation as MutationVideo
from users.schema import Query as QueryUsers , Mutation as MutationUsers

queries = (QueryVideo, QueryUsers)

mutations = (MutationVideo, MutationUsers)

Query = merge_types("Query", queries)

Mutation = merge_types("Mutation", mutations)

schema = Schema(query=Query, mutation=Mutation)
