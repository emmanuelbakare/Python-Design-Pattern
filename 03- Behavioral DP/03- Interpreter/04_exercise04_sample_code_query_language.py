# Context class representing the database records
class DatabaseContext:
    def __init__(self):
        self.records = [
            {'name': 'John', 'age': 25, 'country': 'USA'},
            {'name': 'Jane', 'age': 30, 'country': 'Canada'},
            {'name': 'Bob', 'age': 28, 'country': 'USA'},
             {'name': 'Many', 'age': 22, 'country': 'Canada'},
             {'name': 'Kayode', 'age': 29, 'country': 'Nigeria'},
        ]

# Abstract expression class
class Expression:
    def interpret(self, context):
        pass

# Terminal expression class for selecting a specific field
class FieldExpression(Expression):
    def __init__(self, field_name,index=None):
        self.field_name = field_name
        self.index =index

    def interpret(self, context):
        if not self.index:
            return [record[self.field_name]  for record in context.records]
        elif len(context.records) > self.index and isinstance(self.index, int):
            return [record[self.field_name]  for record in context.records][self.index]
        else:
            return []
        
class FilterExpression(Expression):
    def __init__(self, field_name, operator, value):
        self.field_name = field_name
        self.operator = operator
        self.value = value

    def interpret(self, context):
        filtered_records = []

        for record in context.records:
            if self.operator == '=' and record[self.field_name] == self.value:
                filtered_records.append(record)
            elif self.operator == '>' and record[self.field_name] > self.value:
                filtered_records.append(record)
            elif self.operator == '<' and record[self.field_name] < self.value:
                filtered_records.append(record)
            
        return filtered_records
             

#client Code
if __name__ == '__main__':
    context = DatabaseContext()
    # exp1 = FieldExpression('name',41) 
    # exp1 = FilterExpression('country',"=","Canada")
    # print(exp1.interpret(context)) 

    query = [
        FieldExpression('name'),
        # FieldExpression('age'),
        # FilterExpression('country', '=', 'USA'),
        # FilterExpression('country', '=', 'Nigeria'),
        # FilterExpression('age', '<', 28)
    ]
    
    for expression in query:
         print(expression.interpret(context))
