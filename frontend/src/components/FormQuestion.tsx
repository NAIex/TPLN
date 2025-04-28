import { useEffect, useRef, useState } from 'react';
import { Row, Col, Card, Form } from 'react-bootstrap';
import { FormQuestionProps, FormQuestionType } from '../data/FormQuestionType';
import { FromQuestionCheck } from './FromQuestionCheck';
import { useLocation } from 'react-router-dom';
const FormQuestion = (props: FormQuestionProps) => {
  const [isVisible, setIsVisible] = useState(false);
  const location = useLocation();

  const [disabled, setDisabled] = useState(false);


  const appear = () => {
    setIsVisible(true);
    console.log('triggered');
  }

  useEffect(() => {
    setIsVisible(props.appear);
  }, [props.appear]);

  const getQuestionContent = () => {
    let questionContent;
    switch (props.type) {
      case 'NONE':
        questionContent = null;
        break;
      case 'SHORT_ANSWER':
        questionContent = (
          <Form.Group className="mt-3">
            <Form.Control disabled={disabled} as="textarea" rows={3} placeholder="Detaliați puțin mai mult..." />
          </Form.Group>
        );
        break;
    }
    return questionContent;
  }

  return (
    <Row className="justify-content-center" key={location.key}>
      <Col md={12}>
        <Card className={`form-question text-center ${isVisible ? 'visible' : ''}`}>
          <Card.Body>
            <Card.Title style={{ fontSize: '2rem' }}>{props.question}</Card.Title>
            <Card.Text style={{ fontStyle: 'italic' }}>
              {props.description}
            </Card.Text>
            {props.type !== FormQuestionType.NONE && (
              <FromQuestionCheck onTriggerFunction={setDisabled} onTriggerEvent={props.onTrigger} />
            )}
            {getQuestionContent()}

          </Card.Body>
        </Card>
      </Col>
    </Row>
  );
};

export default FormQuestion;