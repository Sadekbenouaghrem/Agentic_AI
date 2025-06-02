import graphene
import agents.schema

class Query(agents.schema.Query, graphene.ObjectType):
    pass

class Mutation(agents.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
