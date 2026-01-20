import streamlit as SL
import json
import pandas as pd
import io
from utils.APIs import call_gemini_with_retry

def rendert():
    SL.markdown("### Create Your Timetable")
    with SL.form("task_form"):
        col1, col2, col3, col4 = SL.columns(4)
        with col1:
            task_name = SL.text_input("Task Name", placeholder="e.g., Study Math")
        with col2:
            from_datetime = SL.text_input("From (Optional)", placeholder="YYYY-MM-DD HH:MM")
        with col3:
            to_datetime = SL.text_input("To (Optional)", placeholder="YYYY-MM-DD HH:MM")
        with col4:
            est_time = SL.text_input("Estimated Time (Optional)", placeholder="e.g., 2 hours")
        add_task = SL.form_submit_button("➕ Add Task")
        if add_task and task_name:
            SL.session_state.tasks.append({
                "name": task_name,
                "from": from_datetime,
                "to": to_datetime,
                "estimated": est_time
            })
            SL.success(f"Added task: {task_name}")
    if SL.session_state.tasks:
        SL.markdown("#### Current Tasks")
        for i, task in enumerate(SL.session_state.tasks):
            SL.write(f"{i+1}. **{task['name']}** | From: {task['from']} | To: {task['to']} | Est: {task['estimated']}")
        if SL.button("Clear All Tasks"):
            SL.session_state.tasks = []
            SL.rerun()
    total_time = SL.text_input("Estimated Total Time", placeholder="e.g., 8 hours")
    if SL.button("Generate Timetable", type="primary"):
        if SL.session_state.tasks:
            with SL.spinner("Generating timetable..."):
                task_str = json.dumps(SL.session_state.tasks, indent=2)
                prompt = f"""Create a detailed timetable based on these tasks:
{task_str}
Total estimated time available: {total_time}
Generate a realistic schedule in CSV format with these EXACT column headers:
Task Name,Start Time,End Time,Duration,Priority
Provide ONLY the CSV data with proper formatting. Each row should be on a new line.
Example format:
Task Name,Start Time,End Time,Duration,Priority
Study Math,09:00 AM,10:30 AM,1.5 hours,High
Break,10:30 AM,10:45 AM,15 minutes,Medium"""
                result = call_gemini_with_retry(prompt)
                if 'timetable_result' not in SL.session_state:
                    SL.session_state.timetable_result = None
                SL.session_state.timetable_result = result
        else:
            SL.warning("Please add at least one task first!")
    if 'timetable_result' in SL.session_state and SL.session_state.timetable_result:
        SL.markdown("#### Generated Timetable")
        try:
            lines = SL.session_state.timetable_result.strip().split('\n')
            lines = [line for line in lines if not line.strip().startswith('```')]
            header_line = None
            data_lines = []
            for line in lines:
                if 'Task Name' in line or 'task name' in line.lower():
                    header_line = line
                elif line.strip() and ',' in line:
                    data_lines.append(line)
            if header_line and data_lines:
                import csv
                from io import StringIO
                csv_data = header_line + '\n' + '\n'.join(data_lines)
                df = pd.read_csv(StringIO(csv_data))
                SL.dataframe(
                    df,
                    use_container_width=True,
                    height=400,
                    hide_index=True
                )
                SL.markdown("#### Download Timetable")
                col1, col2, col3 = SL.columns(3)
                with col1:
                    excel_buffer = io.BytesIO()
                    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False, sheet_name='Timetable')
                    excel_buffer.seek(0)
                    SL.download_button(
                        label="📥 Download as Excel",
                        data=excel_buffer,
                        file_name="study_timetable.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                with col2:
                    csv_data = df.to_csv(index=False)
                    SL.download_button(
                        label="📥 Download as CSV",
                        data=csv_data,
                        file_name="study_timetable.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                with col3:
                    try:
                        from reportlab.lib import colors
                        from reportlab.lib.pagesizes import letter, A4
                        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
                        from reportlab.lib.styles import getSampleStyleSheet
                        from reportlab.lib.units import inch
                        pdf_buffer = io.BytesIO()
                        doc = SimpleDocTemplate(pdf_buffer, pagesize=A4)
                        elements = []
                        styles = getSampleStyleSheet()
                        title = Paragraph("<b>Study Timetable</b>", styles['Title'])
                        elements.append(title)
                        elements.append(Spacer(1, 0.3*inch))
                        table_data = [df.columns.tolist()] + df.values.tolist()
                        t = Table(table_data)
                        t.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('FONTSIZE', (0, 0), (-1, 0), 12),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                            ('FONTSIZE', (0, 1), (-1, -1), 10),
                            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey])
                        ]))
                        elements.append(t)
                        doc.build(elements)
                        pdf_buffer.seek(0)
                        SL.download_button(
                            label="📥 Download as PDF",
                            data=pdf_buffer,
                            file_name="study_timetable.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )
                    except ImportError:
                        SL.info("PDF download requires 'reportlab'. Install with: pip install reportlab")
            else:
                SL.text_area("Timetable", SL.session_state.timetable_result, height=400)
        except Exception as e:
            SL.text_area("Timetable", SL.session_state.timetable_result, height=400)
            SL.info("Could not parse timetable as table. Displaying as text.")
