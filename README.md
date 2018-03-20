#MLData      
MLData, is a project to clean and normalize data for machine learning process.


## How to install
```pip install mldata```




## Usage Example
Usage Example:    
```
        from mldata import Processor
        new_file_path = "outputs/new.csv"
        processor = Processor("resource/raw_dataset.csv", target_column="APPROVE/NOT", exclude_column_list=["id"],
                              category_list=["Work Class", "FnlWgt", "Education", "Maried Status", "Occupation",
                                             "Relationship", "Race", "Gender", "Native Country", "Flag"],
                              invalid_values=["?", "", "null", None],
                              positive_tag=1)
        processor.normalize()
        processor.save_to_file(new_file_path)
```


## API Description    
1, Init function
```
Processor(csv_file_path, target_column, exclude_column_list=None, category_list=None, positive_tag=1,
                 csv_header=0, invalid_values=None)

```
Parameters:     
csv_file_path: The origin csv file path                
target_column: The column name of the target              
exclude_column_list: Columns no need to normalize       
category_list: A column name list which are category based columns       
positive_tag: The positive tag for the target column value, default value is 1        
invalid_values: values in csv not valid, such as "?", "", "null", None     
            
2, Norm the list
```buildoutcfg
Processor.normalize()   
``` 
This function is used to do norm to the csv file.


3, Save result to csv file.    
```buildoutcfg
Processor.save_to_file(new_file_name)          
``` 
This function is used to save normalized output to csv file.            
Parameters: 
new_file_name: The new file name to save the normalized data             