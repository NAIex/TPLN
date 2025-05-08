import { useEffect, useState } from 'react'

import { Container, Col, Row, Button } from 'react-bootstrap';
import FormQuestion from '../components/FormQuestion';
import { FormQuestionType } from '../data/FormQuestionType';
import { useLocation, useNavigate } from 'react-router-dom';
import { FormResponse, FormStructure, sendForm } from '../utils/formPageFunctions';
import { useLocalStorage } from 'react-use';


export const FormPageRevamped = () => {

    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const [visibleIndex, setVisibleIndex] = useState(0);

    const location = useLocation();

    const [totalFormAnswer, setTotalFormAnswer] = useLocalStorage<{}>('total-form-answer', {})
    const [formAnswer, setFormAnswer] = useState<FormResponse>()

    const [descriptionData, setDescriptionData] = useLocalStorage<string>('description-data', '')
    const [formData, setFormData] = useLocalStorage<FormStructure>('current-form')


    async function updateFormTextData(index, text){
        const data = formAnswer;
        data[index] = text;

        setFormAnswer(data);

    }
    async function updateFormBoolData(index, bool){
        const data = formAnswer;
        console.log(data, index);
        data[index] = bool;
        
        setFormAnswer(data);
    }

    async function sendData(){
        setIsLoading(true)
          const answer = formAnswer;
          const title = formAnswer.form_section;
          delete answer.form_section;
          
          
          const totalForm = totalFormAnswer;
          totalForm[title] = answer;
          setTotalFormAnswer(totalForm);

          let response = await sendForm(descriptionData, totalForm);

          setFormData(response);

          console.log(response);
        setIsLoading(false);
        navigate('/form');
        window.location.reload();

          // pseudo delay
        setTimeout(() => {
        }, 1000);
    }

    useEffect(() => {

        const answer = {} as FormResponse;
        answer.form_section = formData?.form_section;

        formData.items.forEach(element => {
            answer[element.id.toString()-1] = false;
        });
        console.log(answer);
        setFormAnswer(answer);


    },[])


    return (
        <Container key={location.key}>
          <FormQuestion 
            id={0} 
            question="Formular Introductiv" 
            isRequired={false} 
            type={FormQuestionType.NONE}
            appear={true}
          />
          <Row>
          {formData.items.map((value, index) => {
            const onTrigger = () => {
              // Enable the next object in the list by updating its isRequired state
              setVisibleIndex(index + 1);
            };
    
            return (
              <Col md={3} key={index}>
                <FormQuestion
                  id={index} 
                  question_id={value.id}
                  type={FormQuestionType.SHORT_ANSWER}
                  description={value.text} 
                  isRequired={index === 0} // Only the first question is required initially
                  is_critical={value.is_critical} 
                  appear={index <= visibleIndex}
                  onTrigger={onTrigger} // Pass the onTrigger function
                  data-testid={`question-${index}`} // Add a test ID for easier access
    
                  onChangeText={(text) => updateFormTextData(index, text)} // Update the text answer
                  onChangeBool={(val) => updateFormBoolData(value.id-1,val)} // Update the boolean answer
                />
              </Col>
            );
          })}
          </Row>
          <Button variant="dark" className="mt-4" onClick={sendData} disabled={isLoading || visibleIndex < formData.length}>
                        {isLoading ? 'Loading...' : 'Continue'}
          </Button>
        </Container>
    
      );
}
