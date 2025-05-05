import { useState } from 'react'
import { FaTimes } from 'react-icons/fa';
import { Form } from 'react-bootstrap';
import { FaCheck } from 'react-icons/fa';

import '../css/Slider.css'

export const FromQuestionCheck = (props: {onTriggerFunction: (value: boolean) => void, onTriggerEvent: () => void }) => {
  const [isChecked, setIsChecked] = useState(-1); // -1 means nothing selected, 0 means false (X), 1 means true (checkmark)
  
  return (
    <Form.Group>
        <div className="slider-container" style={{ width: '100%', display: 'flex', justifyContent: 'space-between' }}>
            <div className="option" onClick={() => { setIsChecked(1); props.onTriggerFunction(false); props.onTriggerEvent(); }} style={{ cursor: 'pointer', flex: 1, textAlign: 'center' }}>
            <div className={`slider ${isChecked === 1 ? 'checked' : ''}`} style={{ width: '100%', backgroundColor: isChecked === 1 ? '#4caf50' : 'gray', borderTopRightRadius: '0px', borderBottomRightRadius: '0px' }}>
                <span className="slider-icon po-none" style={{ userSelect: 'none', color: isChecked === 1 ? 'white' : 'darkgray' }}><FaCheck /></span>
            </div>
            </div>
            <div className="option" onClick={() => { setIsChecked(0); props.onTriggerFunction(true); props.onTriggerEvent(); }} style={{ cursor: 'pointer', flex: 1, textAlign: 'center' }}>
            <div className={`slider ${isChecked === 0 ? 'checked' : ''}`} style={{ width: '100%', backgroundColor: isChecked === 0 ? '#ff1100' : 'gray', borderTopLeftRadius: '0px', borderBottomLeftRadius: '0px' }}>
                <span className="slider-icon po-none" style={{ userSelect: 'none', color: isChecked === 0 ? 'white' : 'darkgray' }}><FaTimes /></span>
            </div>
            </div>
        </div>
    </Form.Group>
  )
}
